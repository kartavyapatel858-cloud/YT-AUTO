import os
import subprocess
import shutil

master_video = r"d:\Youtube automation\published_masters\episode_05_knuckle_crack.mp4"
temp_video = r"d:\Youtube automation\published_masters\episode_05_knuckle_crack_temp.mp4"

public_audio = r"d:\Youtube automation\remotion-shorts\public\ep5\audio.m4a"
temp_audio = r"d:\Youtube automation\remotion-shorts\public\ep5\audio_temp.m4a"

print("1. Boosting audio in master video by 15% (volume=1.15)...")
cmd_video = [
    "ffmpeg", "-y",
    "-i", master_video,
    "-c:v", "copy",
    "-af", "volume=1.15",
    "-c:a", "aac",
    "-b:a", "320k",
    "-movflags", "faststart",
    temp_video
]
subprocess.run(cmd_video, check=True)

if os.path.exists(temp_video) and os.path.getsize(temp_video) > 1000000:
    shutil.move(temp_video, master_video)
    print("Master video audio successfully boosted and updated!")
else:
    raise RuntimeError("Failed to boost master video audio.")

print("2. Boosting public audio asset by 15%...")
cmd_audio = [
    "ffmpeg", "-y",
    "-i", public_audio,
    "-af", "volume=1.15",
    "-c:a", "aac",
    "-b:a", "256k",
    temp_audio
]
subprocess.run(cmd_audio, check=True)

if os.path.exists(temp_audio) and os.path.getsize(temp_audio) > 100000:
    shutil.move(temp_audio, public_audio)
    print("Public audio.m4a successfully boosted and updated!")
else:
    raise RuntimeError("Failed to boost public audio.")

print("3. Checking new volume profile with volumedetect...")
res = subprocess.run(
    ["ffmpeg", "-i", master_video, "-af", "volumedetect", "-vn", "-sn", "-dn", "-f", "null", "NUL"],
    capture_output=True, text=True
)
for line in res.stderr.splitlines():
    if "mean_volume" in line or "max_volume" in line:
        print(line.strip())
