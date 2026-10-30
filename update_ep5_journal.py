import json
import os
import subprocess

journal_path = r"d:\Youtube automation\production_journal.json"
with open(journal_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Find if episode 5 already exists
ep5_idx = None
for idx, ep in enumerate(data.get("episodes", [])):
    if ep.get("episode") == 5:
        ep5_idx = idx
        break

ep5_entry = {
    "episode": 5,
    "title": "What ACTUALLY Makes Your Knuckles Crack? 💥🦴 #Shorts",
    "url": "Pending upload",
    "master_file": "published_masters/episode_05_knuckle_crack.mp4",
    "citations": [
        "Kawchuk et al. (2015) Real-Time Visualization of Joint Cavitation, PLOS ONE",
        "Unger (1998) Does knuckle cracking lead to arthritis of the fingers?, Arthritis & Rheumatism (Ig Nobel Prize in Medicine 2009)"
    ],
    "key_learning": "100% bespoke 3D medical CGI pipeline with zero slop: 6 dedicated 9:16 anatomical visuals depicting synovial fluid negative pressure, nitrogen vapor cavitation bubble formation, and supersonic acoustic collapse shockwave. Frame-accurate audio slam and damping spring recoil timed exactly to 36.01s (frame 1080). Subtitles centered inside safe zone with #FFE600 active highlights.",
    "file_size": "Pending",
    "duration": "51.55s",
    "resolution": "1080x1920",
    "visual_assets": [
        "public/ep5/shot1_cracking_hand.png (3D CGI Zack D. character bending index knuckle)",
        "public/ep5/shot2_joint_capsule_anatomy.png (3D anatomical MCP joint cutaway & amber synovial fluid)",
        "public/ep5/shot3_vacuum_stretch.png (Mechanical joint capsule expansion under negative pressure)",
        "public/ep5/shot4_cavitation_bubble_forms.png (Microscopic nitrogen cavitation bubble nucleation)",
        "public/ep5/shot5_bubble_collapse_shockwave.png (Supersonic bubble collapse shockwave impact at 36.01s)",
        "public/ep5/shot6_healthy_hands_60years.png (Dr. Donald Unger 60-year dual-hand comparison & X-ray)"
    ]
}

if ep5_idx is not None:
    data["episodes"][ep5_idx] = ep5_entry
else:
    data["episodes"].append(ep5_entry)

with open(journal_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Successfully updated production_journal.json with Episode 5 baseline.")
