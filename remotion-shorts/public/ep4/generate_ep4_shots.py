import urllib.request
import urllib.parse
import os
import subprocess
import time

EP4_DIR = r"d:\Youtube automation\remotion-shorts\public\ep4"
FFMPEG = r"C:\Users\Kartavya\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"

SHOT_PROMPTS = [
    (
        "shot1_bed_falling_void",
        "Zack D Films 3D animation style. A stylized 3D character lying in bed in a dark bedroom, slipping downward into a dark surreal cosmic void. Volumetric cyan and deep amber rim lighting, dark studio background, high resolution 3D CGI, 9:16 vertical aspect ratio"
    ),
    (
        "shot2_brain_sleep_switch",
        "Zack D Films 3D anatomy explainer style. Detailed 3D translucent human head and brain cutaway. Reticular activating system in brainstem fading to dim blue, sleep center glowing in violet sending paralysis signals down the spinal cord. Clean medical CGI aesthetic, subsurface scattering, dark background, 9:16 vertical aspect ratio"
    ),
    (
        "shot3_muscle_fibers_limp",
        "Zack D Films 3D scientific style. Extreme close-up 3D cross-section of skeletal muscle fibers suddenly losing tension, uncoiling and going completely limp and flaccid simultaneously. Delicate tendon anchors relaxing, glowing bio-fibers, dramatic dark studio backdrop, 9:16 vertical aspect ratio"
    ),
    (
        "shot4_brainstem_falling_illusion",
        "Zack D Films 3D animation style. A dramatic split 3D view: on top a stylized brain stem with alert warning indicators flashing amber, below a 3D silhouette of the character plummeting uncontrollably through a dark abyss as if falling off a cliff. High tension, dark background, 9:16 vertical aspect ratio"
    ),
    (
        "shot5_motor_cortex_emergency_shock",
        "Zack D Films 3D medical CGI style. A glowing 3D cross-section of the human brain with the primary motor cortex firing an explosive bright golden-cyan electrical lightning discharge straight down the central spinal cord pathway. Intense electrical branching, neural action potentials, dark background, 9:16 vertical aspect ratio"
    ),
    (
        "shot6_jolt_awake_gasp_bed",
        "Zack D Films 3D style. The 3D character violently jolting upright in bed, hands clutching the blankets, eyes wide open in shock, breathing heavily, snapping awake into reality. Warm bedside lamp rim lighting contrasting with dark shadows, clean 3D character aesthetic, 9:16 vertical aspect ratio"
    )
]

def generate_all():
    print("=== GENERATING EPISODE 4 3D SHOTS ===")
    for idx, (filename, prompt) in enumerate(SHOT_PROMPTS, 1):
        print(f"\n[{idx}/6] Generating {filename}...")
        encoded = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded}?width=576&height=1024&model=turbo&nologo=true&seed={idx*73+19}"
        
        raw_tmp = os.path.join(EP4_DIR, f"temp_{filename}.jpg")
        final_jpg = os.path.join(EP4_DIR, f"{filename}.jpg")
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        success = False
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    data = resp.read()
                    with open(raw_tmp, "wb") as f:
                        f.write(data)
                success = True
                break
            except Exception as e:
                print(f"  Attempt {attempt+1} failed: {e}. Retrying in 2s...")
                time.sleep(2)
                
        if not success:
            print(f"FAILED to generate {filename}")
            continue
            
        # Upscale and sharpen with FFmpeg to 1080x1920
        cmd = [
            FFMPEG, "-y",
            "-i", raw_tmp,
            "-vf", "scale=1080:1920:flags=lanczos,unsharp=5:5:0.7:3:3:0.3",
            final_jpg
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if os.path.exists(raw_tmp):
            os.remove(raw_tmp)
        print(f"  [OK] Saved {final_jpg} ({os.path.getsize(final_jpg)} bytes)")
        time.sleep(1)

    print("\nAll shots generated successfully.")

if __name__ == "__main__":
    generate_all()
