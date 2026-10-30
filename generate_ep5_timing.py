import asyncio
import edge_tts
import json
import os
import subprocess

SCRIPT_TEXT = """What ACTUALLY makes that loud, satisfying crack when you pop your knuckles?

Most people think bones are grinding together, or that this causes arthritis... but that's completely wrong.

Inside your finger joints, two bones meet inside an airtight capsule filled with a slippery liquid called synovial fluid.

When you pull or bend your finger, you force this capsule to stretch open. This creates an instant vacuum!

Under this extreme negative pressure, dissolved nitrogen gas rapidly boils out of the fluid, forming a microscopic bubble.

Within milliseconds, the surrounding fluid rushes back in, violently collapsing the bubble and firing an acoustic shockwave. That shockwave is the loud pop you hear!

And as for arthritis? One doctor cracked only his left hand every day for sixty years. Both hands remained completely healthy!"""

VOICE = "en-US-GuyNeural"
OUTPUT_DIR = r"D:\Youtube automation\remotion-shorts\public\ep5"
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
        # Weight by word length
        total_chars = sum(len(w) for w in raw_words)
        curr_t = start_t
        for w in raw_words:
            w_dur = (len(w) / total_chars) * sent_duration
            words_data.append({
                "word": w,
                "start": round(curr_t, 3),
                "end": round(curr_t + w_dur, 3)
            })
            curr_t += w_dur
            
    # Get audio duration via ffprobe
    res = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", RAW_AUDIO_PATH
    ], capture_output=True, text=True, check=True)
    audio_dur = float(res.stdout.strip())
    
    result = {
        "duration": audio_dur,
        "sentences": boundaries,
        "words": words_data
    }
    
    with open(TRANSCRIPT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        
    print(f"Transcript written to {TRANSCRIPT_JSON_PATH}. Total duration: {audio_dur:.2f}s")
    return audio_dur, boundaries, words_data

def mix_master_audio(duration, words_data):
    print("Mixing master audio with BGM and sound effects...")
    bgm_path = r"D:\Youtube automation\assets\music\dark_synth_drive.mp3"
    pop_sfx = r"D:\Youtube automation\core\openmontage\.agents\skills\hyperframes-media\assets\sfx\pop.mp3"
    impact_sfx = r"D:\Youtube automation\core\openmontage\.agents\skills\hyperframes-media\assets\sfx\impact-bass-1.mp3"
    
    # Find timestamp for "collapsing" or "shockwave"
    pop_time = 34.0
    for w in words_data:
        if "collapsing" in w["word"].lower():
            pop_time = w["start"]
            break
            
    print(f"Cavitation pop timestamp: {pop_time:.2f}s")
    delay_ms = int(pop_time * 1000)
    
    cmd = [
        "ffmpeg", "-y",
        "-i", RAW_AUDIO_PATH,
        "-stream_loop", "-1", "-i", bgm_path,
        "-i", pop_sfx,
        "-i", impact_sfx,
        "-filter_complex",
        f"[0:a]volume=1.0[vocal];"
        f"[1:a]volume=0.13,atrim=0:{duration + 0.5},afade=t=out:st={duration - 1.5}:d=1.5[bgm];"
        f"[2:a]adelay={delay_ms}|{delay_ms},volume=1.4[pop];"
        f"[3:a]adelay={delay_ms}|{delay_ms},volume=1.1[bass];"
        f"[vocal][bgm][pop][bass]amix=inputs=4:duration=first:dropout_transition=2[outa]",
        "-map", "[outa]",
        "-c:a", "aac",
        "-b:a", "256k",
        MASTER_AUDIO_PATH
    ]
    
    subprocess.run(cmd, check=True)
    print(f"Master audio saved to {MASTER_AUDIO_PATH}")

if __name__ == "__main__":
    dur, bnd, words = asyncio.run(generate_speech_and_boundaries())
    mix_master_audio(dur, words)
