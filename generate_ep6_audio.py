import asyncio
import edge_tts
import json
import os
import subprocess

SCRIPT_TEXT = """Have you ever sat on your foot, stood up, and felt like your leg was made of dead rubber?

Then, seconds later, an intense burning prickle rushes in like thousands of tiny electric needles!

Most people think you cut off blood circulation... but that's actually a myth.

Running through your leg are major nerve bundles packed with thousands of microscopic sensory fibers. When you sit awkwardly, you physically crush this nerve against bone.

This compression starves the nerve fibers of oxygen, choking off the electrical signals to your brain. Your foot goes numb.

When you finally stand up and release the pressure, oxygen suddenly floods back in! As the starved neurons reboot, they fire wildly and uncontrollably like chaotic static electricity!

Your brain can't decode this sudden avalanche of random signals, so it translates the chaos as that sharp, prickly burning sensation until the nerve pathway stabilizes!"""

VOICE = "en-US-GuyNeural"
OUTPUT_DIR = r"D:\Youtube automation\remotion-shorts\public\ep6"
os.makedirs(OUTPUT_DIR, exist_ok=True)

RAW_AUDIO_PATH = os.path.join(OUTPUT_DIR, "narration_raw.mp3")
MASTER_AUDIO_PATH = os.path.join(OUTPUT_DIR, "audio.m4a")
TRANSCRIPT_JSON_PATH = os.path.join(OUTPUT_DIR, "transcript.json")

async def generate_speech_and_boundaries():
    print("Generating speech and sentence boundaries with edge-tts...")
    communicate = edge_tts.Communicate(SCRIPT_TEXT, VOICE, rate="+2%", pitch="+0Hz")
    
    boundaries = []
    audio_chunks = []
    
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_chunks.append(chunk["data"])
        elif chunk["type"] == "SentenceBoundary":
            boundaries.append({
                "start": round(chunk["offset"] / 10_000_000, 3),
                "duration": round(chunk["duration"] / 10_000_000, 3),
                "end": round((chunk["offset"] + chunk["duration"]) / 10_000_000, 3),
                "text": chunk["text"].strip()
            })
            
    with open(RAW_AUDIO_PATH, "wb") as f:
        for chunk in audio_chunks:
            f.write(chunk)
            
    print(f"Saved audio ({len(audio_chunks)} chunks) to {RAW_AUDIO_PATH}")
    print(f"Captured {len(boundaries)} sentence boundaries.")
    
    # Generate word-level timing by interpolating each sentence's words across its duration
    words_data = []
    for b in boundaries:
        raw_words = [w.strip() for w in b["text"].split() if w.strip()]
        if not raw_words:
            continue
        sent_duration = b["duration"]
        start_t = b["start"]
        
        # Word length weighting
        total_chars = sum(max(1, len(w.rstrip(".,!?;:\"'"))) for w in raw_words)
        curr_t = start_t
        for i, w in enumerate(raw_words):
            clean_len = max(1, len(w.rstrip(".,!?;:\"'")))
            w_dur = round(sent_duration * (clean_len / total_chars), 3)
            # Ensure minimum duration
            w_dur = max(0.18, w_dur)
            w_end = round(curr_t + w_dur, 3)
            if i == len(raw_words) - 1:
                w_end = b["end"]
            
            clean_word = w.strip(".,!?;:\"'")
            words_data.append({
                "word": clean_word,
                "punctuated": w,
                "start": curr_t,
                "end": w_end
            })
            curr_t = w_end

    total_dur = boundaries[-1]["end"] if boundaries else 0.0
    print(f"Total narration duration: {total_dur:.2f}s ({len(words_data)} words)")
    
    result = {
        "duration": total_dur,
        "sentences": boundaries,
        "words": words_data
    }
    
    with open(TRANSCRIPT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        
    return total_dur, boundaries, words_data

def mix_master_audio(duration, words):
    print("Mixing master audio with BGM and sound effects...")
    bgm_path = r"D:\Youtube automation\assets\music\dark_synth_drive.mp3"
    glitch_sfx = r"D:\Youtube automation\core\openmontage\.agents\skills\hyperframes-media\assets\sfx\glitch-1.mp3"
    sub_drop_sfx = r"D:\Youtube automation\assets\sfx\sub_drop.wav"
    impact_sfx = r"D:\Youtube automation\core\openmontage\.agents\skills\hyperframes-media\assets\sfx\impact-bass-1.mp3"
    
    # Find timestamp for the climax: "reboot" or "chaotic"
    reboot_time = 32.0
    for w in words:
        if "reboot" in w["word"].lower():
            reboot_time = w["start"]
            break
            
    print(f"Reboot / pins-and-needles rush timestamp: {reboot_time:.2f}s")
    delay_reboot_ms = int(reboot_time * 1000)
    
    # We apply the user's requested +15% boost baseline (volume=1.15) to vocal
    cmd = [
        "ffmpeg", "-y",
        "-i", RAW_AUDIO_PATH,
        "-stream_loop", "-1", "-i", bgm_path,
        "-i", glitch_sfx,
        "-i", impact_sfx,
        "-filter_complex",
        f"[0:a]volume=1.15[vocal];"
        f"[1:a]volume=0.14,atrim=0:{duration + 0.5},afade=t=out:st={duration - 1.5}:d=1.5[bgm];"
        f"[2:a]adelay={delay_reboot_ms}|{delay_reboot_ms},volume=1.2[glitch];"
        f"[3:a]adelay={delay_reboot_ms}|{delay_reboot_ms},volume=0.9[bass];"
        f"[vocal][bgm][glitch][bass]amix=inputs=4:duration=first:dropout_transition=2[outa]",
        "-map", "[outa]",
        "-c:a", "aac",
        "-b:a", "320k",
        MASTER_AUDIO_PATH
    ]
    
    subprocess.run(cmd, check=True)
    print(f"Master audio saved to {MASTER_AUDIO_PATH}")

if __name__ == "__main__":
    dur, bnd, words = asyncio.run(generate_speech_and_boundaries())
    mix_master_audio(dur, words)
