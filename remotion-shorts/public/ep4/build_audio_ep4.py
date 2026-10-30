import asyncio
import edge_tts
import json
import numpy as np
import subprocess
import os

EP4_DIR = r"d:\Youtube automation\remotion-shorts\public\ep4"
FFMPEG = r"C:\Users\Kartavya\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"

VOICE = "en-US-GuyNeural"
RATE = "+1%"
PITCH = "+0Hz"

SCRIPT_TEXT = (
    "Ever started drifting off to sleep, only to feel yourself falling and violently jerk awake? "
    "That terrifying jolt is called a hypnic jerk, and over seventy percent of all humans experience it. "
    "As you fall asleep, your brain initiates sleep paralysis so you don't physically act out your dreams. "
    "Your breathing slows, your brainwaves drop, and your muscles completely relax. "
    "But sometimes, your awake system and your sleep system battle for control during the handoff. "
    "When your muscles go limp too quickly, your confused brain stem misinterprets the sudden drop in tension as literally tumbling through mid-air! "
    "In a sheer panic to save your life, your motor cortex fires an explosive emergency shock straight down your spinal cord to catch yourself, "
    "violently snapping you back to reality before you ask..."
)

async def generate_narration():
    print("Generating GuyNeural narration...")
    communicate = edge_tts.Communicate(SCRIPT_TEXT, VOICE, rate=RATE, pitch=PITCH)
    raw_audio = os.path.join(EP4_DIR, "raw_narration.mp3")
    
    subtitles = []
    with open(raw_audio, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "SentenceBoundary":
                subtitles.append({
                    "start": chunk["offset"] / 10_000_000.0,
                    "duration": chunk["duration"] / 10_000_000.0,
                    "end": (chunk["offset"] + chunk["duration"]) / 10_000_000.0,
                    "text": chunk["text"]
                })
                
    subs_path = os.path.join(EP4_DIR, "subtitles.json")
    with open(subs_path, "w", encoding="utf-8") as f:
        json.dump(subtitles, f, indent=2)
    print(f"Saved {subs_path} ({len(subtitles)} sentence blocks)")
    return raw_audio, subtitles

def get_audio_duration(file_path):
    cmd = [
        os.path.join(os.path.dirname(FFMPEG), "ffprobe.exe"),
        "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", file_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return float(res.stdout.strip())

def generate_hypnic_soundtrack(duration_sec):
    print(f"Generating hypnic jerk suspense soundtrack for {duration_sec:.2f}s...")
    sample_rate = 44100
    num_samples = int(duration_sec * sample_rate)
    t = np.linspace(0, duration_sec, num_samples, endpoint=False)
    
    # 1. Opening hook sub-bass impact drop (0 to 1.3s)
    hook_drop = np.zeros(num_samples)
    hlen = int(1.3 * sample_rate)
    ht = np.linspace(0, 1.3, hlen)
    sfreq = np.linspace(75, 38, hlen)
    hook_drop[:hlen] = np.sin(2 * np.pi * sfreq * ht) * np.exp(-ht * 2.2) * 0.4
    
    # 2. Dreamy slow delta/theta pulse (representing falling asleep)
    theta_bass = np.zeros(num_samples)
    chord_len = int(7.5 * sample_rate)
    bass_notes = [65.41, 55.00, 48.99, 43.65] # C2, A1, G1, F1
    for i in range(0, num_samples, chord_len):
        chunk = min(chord_len, num_samples - i)
        f = bass_notes[(i // chord_len) % len(bass_notes)]
        ct = t[i:i+chunk] - t[i]
        sine = np.sin(2 * np.pi * f * ct) + 0.25 * np.sin(2 * np.pi * f * 2 * ct)
        env = np.sin(np.pi * np.linspace(0, 1, chunk))
        theta_bass[i:i+chunk] += sine * env * 0.35
        
    # 3. Eerie drifting ethereal synth pad (sleep drifting)
    pad_signal = np.zeros(num_samples)
    pad_chords = [
        [130.81, 155.56, 196.00, 246.94], # Cm(maj7) dreamy/mysterious
        [110.00, 130.81, 164.81, 196.00], # Am7
        [98.00, 123.47, 146.83, 185.00],  # Gm(add9)
        [87.31, 110.00, 130.81, 174.61]   # Fmaj7
    ]
    for i in range(0, num_samples, chord_len):
        chunk = min(chord_len, num_samples - i)
        chord = pad_chords[(i // chord_len) % len(pad_chords)]
        ct = t[i:i+chunk] - t[i]
        c_audio = np.zeros(chunk)
        for freq in chord:
            c_audio += (np.sin(2 * np.pi * freq * ct) + np.sin(2 * np.pi * (freq * 1.002) * ct)) * 0.08
        env = np.sin(np.pi * np.linspace(0, 1, chunk))
        pad_signal[i:i+chunk] += c_audio * env * 0.3
        
    # 4. The Explosive "Jerk" Transient at t ~ 34s (where the motor cortex shocks the body)
    jerk_impact = np.zeros(num_samples)
    jerk_time = 34.0
    if jerk_time < duration_sec:
        jidx = int(jerk_time * sample_rate)
        jlen = int(1.2 * sample_rate)
        if jidx + jlen < num_samples:
            jt = np.linspace(0, 1.2, jlen)
            # High punch 90Hz to 35Hz sub slam + sharp transient
            slam = np.sin(2 * np.pi * np.linspace(120, 35, jlen) * jt) * np.exp(-jt * 3.5) * 0.6
            noise = np.random.uniform(-0.15, 0.15, jlen) * np.exp(-jt * 18.0)
            jerk_impact[jidx:jidx+jlen] = slam + noise

    mix = hook_drop + theta_bass + pad_signal + jerk_impact
    max_v = np.max(np.abs(mix))
    if max_v > 0:
        mix = (mix / max_v) * 0.32
        
    pcm = (mix * 32767).astype(np.int16).tobytes()
    raw_music = os.path.join(EP4_DIR, "raw_music.mp3")
    cmd = [
        FFMPEG, "-y",
        "-f", "s16le", "-ar", str(sample_rate), "-ac", "1", "-i", "-",
        "-c:a", "libmp3lame", "-b:a", "192k", raw_music
    ]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.communicate(pcm)
    return raw_music

def mix_audio(narration_path, music_path):
    print("Mixing final master audio...")
    output_path = os.path.join(EP4_DIR, "audio.m4a")
    cmd = [
        FFMPEG, "-y",
        "-i", narration_path,
        "-i", music_path,
        "-filter_complex",
        "[1:a]volume=0.14[bg];[0:a][bg]amix=inputs=2:duration=first:dropout_transition=2[aout]",
        "-map", "[aout]",
        "-c:a", "aac", "-b:a", "192k",
        output_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Master audio saved to {output_path}")

async def main():
    narration_file, subs = await generate_narration()
    dur = get_audio_duration(narration_file)
    print(f"Narration duration: {dur:.2f}s")
    music_file = generate_hypnic_soundtrack(dur + 2.0)
    mix_audio(narration_file, music_file)
    # Clean up raw files
    if os.path.exists(narration_file): os.remove(narration_file)
    if os.path.exists(music_file): os.remove(music_file)
    print("Audio production complete.")

if __name__ == "__main__":
    asyncio.run(main())
