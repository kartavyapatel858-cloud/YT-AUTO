import os
import glob
import subprocess
import json
import shutil

artifact_dir = r"C:\Users\Kartavya\.gemini\antigravity\brain\8b92f3a4-dcf5-4f68-be3b-563b23a7bbe4"
target_master = r"d:\Youtube automation\published_masters\episode_05_knuckle_crack.mp4"

# Check where the rendered video ended up
possible_paths = [
    target_master,
    r"d:\Youtube automation\remotion-shorts\.mp4",
    r"d:\Youtube automation\remotion-shorts\episode_05_knuckle_crack.mp4",
    r"d:\Youtube automation\remotion-shorts\out.mp4",
]

found_file = None
for p in possible_paths:
    if os.path.exists(p) and os.path.getsize(p) > 1000000:
        found_file = p
        break

if not found_file:
    # Search for recently modified mp4 files in remotion-shorts or published_masters
    candidates = glob.glob(r"d:\Youtube automation\remotion-shorts\*.mp4") + glob.glob(r"d:\Youtube automation\published_masters\*.mp4")
    candidates = sorted(candidates, key=os.path.getmtime, reverse=True)
    if candidates and os.path.getmtime(candidates[0]) > (os.path.getmtime(__file__) - 300):
        found_file = candidates[0]

print(f"Found rendered candidate: {found_file}")

if found_file and found_file != target_master:
    print(f"Moving {found_file} -> {target_master}")
    shutil.move(found_file, target_master)
    found_file = target_master

if found_file and os.path.exists(found_file):
    size_mb = os.path.getsize(found_file) / (1024 * 1024)
    print(f"Master file exists: {found_file} ({size_mb:.2f} MB)")

    # Run ffprobe
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size,bit_rate:stream=width,height,r_frame_rate,codec_name",
        "-of", "json",
        found_file
    ]
    res = subprocess.run(probe_cmd, capture_output=True, text=True)
    probe_data = json.loads(res.stdout) if res.stdout else {}
    print("Probe output:", json.dumps(probe_data, indent=2))

    # Extract verification frames
    timestamps = [
        ("hook_0_5s", "00:00:00.500"),
        ("anatomy_10s", "00:00:10.000"),
        ("vacuum_20s", "00:00:20.000"),
        ("bubble_28s", "00:00:28.000"),
        ("climax_shockwave_36s", "00:00:36.010"),
        ("resolution_45s", "00:00:45.000")
    ]

    for label, ts in timestamps:
        out_still = os.path.join(artifact_dir, f"ep5_master_{label}.png")
        extract_cmd = [
            "ffmpeg", "-y", "-ss", ts, "-i", found_file,
            "-vframes", "1", "-q:v", "2", out_still
        ]
        subprocess.run(extract_cmd, capture_output=True)
        if os.path.exists(out_still):
            print(f"Extracted {label}: {out_still} ({os.path.getsize(out_still)} bytes)")
        else:
            print(f"Failed to extract {label}")

    # Update production journal
    journal_path = r"d:\Youtube automation\production_journal.json"
    with open(journal_path, "r", encoding="utf-8") as f:
        journal = json.load(f)

    for ep in journal.get("episodes", []):
        if ep.get("episode") == 5:
            ep["file_size"] = f"{size_mb:.1f} MB"
            break

    with open(journal_path, "w", encoding="utf-8") as f:
        json.dump(journal, f, indent=2, ensure_ascii=False)
    print("Updated production_journal.json with verified file size.")
else:
    print("Master file not found yet.")
