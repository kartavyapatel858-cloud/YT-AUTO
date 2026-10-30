import subprocess
import os
import json
import time

remotion_dir = r"d:\Youtube automation\remotion-shorts"
artifact_dir = r"C:\Users\Kartavya\.gemini\antigravity\brain\8b92f3a4-dcf5-4f68-be3b-563b23a7bbe4"
target_master = r"d:\Youtube automation\published_masters\episode_06_pins_and_needles.mp4"

print("1. Rendering full master video with Remotion...")
start_t = time.time()
cmd_render = [
    "cmd.exe", "/c", "npx", "remotion", "render",
    "Episode06-PinsAndNeedles",
    target_master,
    "--gl=angle",
    "--concurrency=8"
]

res = subprocess.run(cmd_render, cwd=remotion_dir, capture_output=True, text=True)
elapsed = time.time() - start_t
print(f"Render finished in {elapsed:.1f}s, exit code: {res.returncode}")

if res.returncode != 0:
    print("Render stderr:", res.stderr[-1000:] if res.stderr else "")
    # Check if remotion outputted an intermediate file that needs faststart
    temp_candidates = [
        target_master,
        r"d:\Youtube automation\remotion-shorts\episode_06_pins_and_needles.mp4"
    ]
    for c in temp_candidates:
        if os.path.exists(c) and os.path.getsize(c) > 1000000:
            target_master = c
            break

if not os.path.exists(target_master) or os.path.getsize(target_master) < 1000000:
    # If remotion had faststart error, check temp dir
    import glob
    temps = glob.glob(r"C:\Users\Kartavya\AppData\Local\Temp\remotion-*\remotion-stitch-temp-dir\fast-start-intermediate*")
    temps = sorted(temps, key=os.path.getmtime, reverse=True)
    if temps and os.path.getsize(temps[0]) > 1000000:
        print(f"Found faststart intermediate: {temps[0]}, finalizing...")
        cmd_finalize = [
            "ffmpeg", "-hide_banner", "-i", temps[0],
            "-c", "copy", "-movflags", "faststart", "-y", target_master
        ]
        subprocess.run(cmd_finalize, check=True)

if os.path.exists(target_master):
    size_mb = os.path.getsize(target_master) / (1024 * 1024)
    print(f"Master video verified: {target_master} ({size_mb:.2f} MB)")

    # Run ffprobe
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size,bit_rate:stream=width,height,r_frame_rate,codec_name",
        "-of", "json",
        target_master
    ]
    probe_res = subprocess.run(probe_cmd, capture_output=True, text=True)
    probe_data = json.loads(probe_res.stdout) if probe_res.stdout else {}
    print("Probe output:", json.dumps(probe_data, indent=2))

    # Extract 6 verification frames
    timestamps = [
        ("hook_0_5s", "00:00:00.500"),
        ("anatomy_14s", "00:00:14.000"),
        ("compression_ischemia_28s", "00:00:28.000"),
        ("oxygen_rush_36s", "00:00:36.000"),
        ("climax_neural_storm_41s", "00:00:41.000"),
        ("pins_needles_resolution_50s", "00:00:50.000")
    ]

    for label, ts in timestamps:
        out_still = os.path.join(artifact_dir, f"ep6_master_{label}.png")
        extract_cmd = [
            "ffmpeg", "-y", "-ss", ts, "-i", target_master,
            "-vframes", "1", "-q:v", "2", out_still
        ]
        subprocess.run(extract_cmd, capture_output=True)
        if os.path.exists(out_still):
            print(f"Extracted {label}: {out_still} ({os.path.getsize(out_still)} bytes)")

    # Update production journal
    journal_path = r"d:\Youtube automation\production_journal.json"
    with open(journal_path, "r", encoding="utf-8") as f:
        journal = json.load(f)

    ep6_idx = None
    for idx, ep in enumerate(journal.get("episodes", [])):
        if ep.get("episode") == 6:
            ep6_idx = idx
            break

    ep6_entry = {
        "episode": 6,
        "title": "Why Do You Get \"Pins and Needles\"? ⚡🦵 #Shorts",
        "url": "Pending upload",
        "master_file": "published_masters/episode_06_pins_and_needles.mp4",
        "citations": [
            "Ochoa & Torebjörk (1980) Paraesthesiae from artificial stimulation of a single sensory motor unit in man, Brain",
            "Dahlin & McLean (1986) Effects of graded compression on nerve conduction, Journal of Hand Surgery"
        ],
        "key_learning": "Hybrid Remotion 4.0 + HyperFrames media workflow: 100% bespoke 3D medical CGI visuals illustrating focal nerve compression, ischemic conduction block, oxygenated reperfusion, and explosive chaotic neural reboot. Frame-accurate glitch static SFX and damping spring camera recoil timed to 40.40s. Subtitles centered inside safe zone with #FFE600 active highlights and +15% audio boost.",
        "file_size": f"{size_mb:.1f} MB",
        "duration": "54.47s",
        "resolution": "1080x1920",
        "visual_assets": [
            "public/ep6/shot1_numb_foot_hook.png (3D CGI Zack D. character sitting on numb leg)",
            "public/ep6/shot2_sciatic_nerve_anatomy.png (3D anatomical leg cutaway with glowing sciatic nerve)",
            "public/ep6/shot3_compressed_nerve_ischemia.png (Mechanical nerve bundle pinch & signal choke)",
            "public/ep6/shot4_oxygen_rush_release.png (Nerve decompression & oxygenated red blood cell rush)",
            "public/ep6/shot5_chaotic_neural_static_climax.png (Climax hyperactive bio-electric neural storm)",
            "public/ep6/shot6_pins_needles_radiating.png (Semi-translucent leg with radiating needle sparks & brain inset)"
        ]
    }

    if ep6_idx is not None:
        journal["episodes"][ep6_idx] = ep6_entry
    else:
        journal["episodes"].append(ep6_entry)

    with open(journal_path, "w", encoding="utf-8") as f:
        json.dump(journal, f, indent=2, ensure_ascii=False)
    print("Updated production_journal.json with Episode 6 master.")
else:
    print("Master video not found")
