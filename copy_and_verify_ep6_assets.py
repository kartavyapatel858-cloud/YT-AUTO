import os
import shutil
import subprocess

artifact_dir = r"C:\Users\Kartavya\.gemini\antigravity\brain\8b92f3a4-dcf5-4f68-be3b-563b23a7bbe4"
target_dir = r"D:\Youtube automation\remotion-shorts\public\ep6"
os.makedirs(target_dir, exist_ok=True)

asset_map = {
    "shot1_numb_foot_hook.png": "shot1_numb_foot_hook_1793355633165.jpg",
    "shot2_sciatic_nerve_anatomy.png": "shot2_sciatic_nerve_anatomy_1793355654865.jpg",
    "shot3_compressed_nerve_ischemia.png": "shot3_compressed_nerve_ischemia_1793355687659.jpg",
    "shot4_oxygen_rush_release.png": "shot4_oxygen_rush_release_1793355711346.jpg",
    "shot5_chaotic_neural_static_climax.png": "shot5_chaotic_neural_static_climax_1793355737259.jpg",
    "shot6_pins_needles_radiating.png": "shot6_pins_needles_radiating_1793355761695.jpg"
}

for target_name, src_name in asset_map.items():
    src_path = os.path.join(artifact_dir, src_name)
    dst_path = os.path.join(target_dir, target_name)
    if os.path.exists(src_path):
        # Convert/copy to PNG using ffmpeg or direct copy
        cmd = ["ffmpeg", "-y", "-i", src_path, dst_path]
        subprocess.run(cmd, check=True)
        size_kb = os.path.getsize(dst_path) / 1024
        print(f"Copied {src_name} -> {target_name} ({size_kb:.1f} KB)")
    else:
        print(f"MISSING: {src_path}")

print("All Episode 6 visual assets ready.")
