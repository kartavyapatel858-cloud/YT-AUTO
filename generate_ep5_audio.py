import asyncio
import edge_tts
import json
import os
import subprocess
from faster_whisper import WhisperModel

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

async def generate_speech():
    print("Generating speech with edge-tts...")
    communicate = edge_tts.Communicate(SCRIPT_TEXT, VOICE, rate="+2%", pitch="+0Hz")
    await communicate.save(RAW_AUDIO_PATH)
    print(f"Speech generated at {RAW_AUDIO_PATH}")

def transcribe_and_align():
    print("Transcribing with faster-whisper...")
    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, info = model.transcribe(RAW_AUDIO_PATH, word_timestamps=True)
    
    words_data = []
    full_transcript = []
    
    for segment in segments:
        for word in segment.words:
            clean_word = word.word.strip()
            if clean_word:
                words_data.append({
                    "word": clean_word,
                    "start": round(word.start, 3),
                    "end": round(word.end, 3),
                    "probability": round(word.probability, 3)
                })
        full_transcript.append({
            "start": round(segment.start, 3),
            "end": round(segment.end, 3),
            "text": segment.text.strip()
        })
        
    print(f"Detected {len(words_data)} words. Total duration: {info.duration:.2f}s")
    
    result = {
        "duration": info.duration,
        "words": words_data,
        "segments": full_transcript
    }
    
    with open(TRANSCRIPT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        
    return info.duration, words_data

def mix_master_audio(duration):
    print("Mixing master audio with BGM and sound effects...")
    bgm_path = r"D:\Youtube automation\assets\music\dark_synth_drive.mp3"
    pop_sfx = r"D:\Youtube automation\core\openmontage\.agents\skills\hyperframes-media\assets\sfx\pop.mp3"
    impact_sfx = r"D:\Youtube automation\core\openmontage\.agents\skills\hyperframes-media\assets\sfx\impact-bass-1.mp3"
    
    # We find the timestamp for "collapsing" or "shockwave"
    # Typically around shot 5 (~32-34s)
    with open(TRANSCRIPT_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    pop_time = 32.5
    for w in data["words"]:
        if "collapsing" in w["word"].lower():
            pop_time = w["start"]
            break
            
    print(f"Cavitation pop timestamp: {pop_time:.2f}s")
    
    # ffmpeg mix:
    # 0: narration (volume 1.0)
    # 1: bgm (ducked to volume 0.13, looped/trimmed to duration)
    # 2: pop sfx delayed to pop_time
    # 3: impact bass delayed to pop_time
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
        f"[2:a]adelay={delay_ms}|{delay_ms},volume=1.3[pop];"
        f"[3:a]adelay={delay_ms}|{delay_ms},volume=0.9[bass];"
        f"[vocal][bgm][pop][bass]amix=inputs=4:duration=first:dropout_transition=2[outa]",
        "-map", "[outa]",
        "-c:a", "aac",
        "-b:a", "256k",
        MASTER_AUDIO_PATH
    ]
    
    subprocess.run(cmd, check=True)
    print(f"Master audio saved to {MASTER_AUDIO_PATH}")

if __name__ == "__main__":
    asyncio.run(generate_speech())
    dur, words = transcribe_and_align()
    mix_master_audio(dur)
