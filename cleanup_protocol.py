import os
import shutil
import json
import glob

WORKSPACE = r"d:\Youtube automation"
REMOTION_DIR = os.path.join(WORKSPACE, "remotion-shorts")
MASTERS_DIR = os.path.join(WORKSPACE, "published_masters")
BRANDING_DIR = os.path.join(WORKSPACE, "branding")
JOURNAL_FILE = os.path.join(WORKSPACE, "production_journal.json")

# Ensure required directories exist
os.makedirs(MASTERS_DIR, exist_ok=True)
os.makedirs(BRANDING_DIR, exist_ok=True)

# 1. Update / Persist the Knowledge Journal
LEARNINGS_DATABASE = {
  "channel": {
    "name": "NEUROCORE 3D",
    "handle": "@NeuroCore3D",
    "topic": "3D Science, Neuroscience & Human Anatomy Explainers (Zack D. Films style)",
    "specs": {
      "resolution": "1080x1920",
      "aspect_ratio": "9:16",
      "target_fps": 30,
      "ideal_duration": "42-46s",
      "voice_narrator": "en-US-GuyNeural (+1% rate, +0Hz pitch)",
      "captions": "Impact 54pt uppercase, WebkitTextStroke 2.6px #000, active word #FFE600 with spring micro-overshoot, 900x1400 safe area at top 1380px",
      "audio_mix": "Soundtrack ducked to -18dB (0.14 volume) under speech, master normalized"
    },
    "critical_visual_rules": [
      "NO 2D geometric vector ripple rings/radar circles over characters/organs. They look cheap and amateurish.",
      "Use physical spring camera jolts/shakes (damping spring) on shock impact frames for visceral weight.",
      "NO low-res turbo diffusion artifacts. Ground visual assets in studio 3D references first.",
      "All text and focal action must sit strictly inside the 900x1400 center box, clearing bottom 320px for YouTube UI.",
      "Remotion composition IDs must only use hyphens and alphanumeric characters (NO underscores).",
      "Always include formal peer-reviewed research citations in description.",
      "Always set COPPA audience to 'No, it is not made for kids'."
    ]
  },
  "episodes": [
    {
      "episode": 1,
      "title": "Why You Can't Tickle Yourself! 🧠⚡ #Shorts",
      "url": "https://youtube.com/shorts/XP3knS_0qn0",
      "master_file": "published_masters/ep01_tickle.mp4",
      "citations": ["Blakemore et al. (1998) Nature Neuroscience", "Blakemore et al. (2000) NeuroReport"],
      "key_learning": "Established Zack D. Films 3D CGI aesthetic, subsurface scattering cutaways, and efference copy science."
    },
    {
      "episode": 2,
      "title": "What ACTUALLY Causes Brain Freeze? 🍦⚡ #Shorts",
      "url": "https://youtube.com/shorts/IWmlIKNaI6I",
      "master_file": "published_masters/ep02_brain_freeze.mp4",
      "citations": ["Serrador et al. (2012) FASEB Journal", "Kaczorowski & Kaczorowski (2002) BMJ"],
      "key_learning": "Transitioned narrator permanently to GuyNeural. Replaced 2D blue concentric rings with physical camera recoil."
    },
    {
      "episode": 3,
      "title": "Why You Get Goosebumps When Scared! 😱⚡ #Shorts",
      "url": "https://youtube.com/shorts/UUmsy6bSoiY",
      "master_file": "published_masters/ep03_goosebumps.mp4",
      "citations": ["Cannon (1929) Bodily Changes in Pain, Hunger, Fear and Rage", "Zhang et al. (2020) Cell/Nature"],
      "key_learning": "Fully migrated animation pipeline to Remotion 4.0 React engine with spring physics and zero vector rings."
    },
    {
      "episode": 4,
      "title": "Why Do You Jerk Awake Just Before Sleeping? (The Hypnic Jerk) ⚡💤 #Shorts",
      "url": "Pending upload",
      "master_file": "published_masters/ep04_hypnic_jerk.mp4",
      "citations": ["Vetrugno & Montagna (2011) Sleep Medicine", "Broughton (1988) Sleep"],
      "key_learning": "Integrated motion design skills (remotion-video, short-form-video, caption-animation, beat-sync-editing, animation-principles). Eliminated low-res artifacts with verified 3D translucent anatomy, kinetic spring pop-in typography, and beat-synced 36s impact recoil."
    }
  ]
}

def archive_and_clean():
    print("=== EXECUTING NEUROCORE 3D CLEANUP PROTOCOL ===")
    
    # Save Knowledge Journal
    with open(JOURNAL_FILE, "w", encoding="utf-8") as f:
        json.dump(LEARNINGS_DATABASE, f, indent=2)
    print(f"[OK] Knowledge Journal saved to {JOURNAL_FILE}")
    
    # Archive Masters
    master_copies = [
        ("final_short_zack_edition.mp4", os.path.join(MASTERS_DIR, "ep01_tickle.mp4")),
        ("episode_02_brain_freeze.mp4", os.path.join(MASTERS_DIR, "ep02_brain_freeze.mp4")),
        ("episode_03_goosebumps.mp4", os.path.join(MASTERS_DIR, "ep03_goosebumps.mp4")),
        (os.path.join(REMOTION_DIR, "episode_04_hypnic_jerk.mp4"), os.path.join(MASTERS_DIR, "ep04_hypnic_jerk.mp4")),
    ]
    for src_path, dest_path in master_copies:
        if not os.path.isabs(src_path):
            src_path = os.path.join(WORKSPACE, src_path)
        if os.path.exists(src_path):
            shutil.copy2(src_path, dest_path)
            print(f"[ARCHIVED] {os.path.basename(src_path)} -> {dest_path}")
            
    # Purge scratch test files in Remotion directory
    remotion_purge = [
        "test_three.png",
        "ep4_frame_jolt.png",
        "ep4_jolt_clip.mp4",
        "clean_frame_*.png",
        "test_frame_*.png",
        "ep3_frame_*.png",
        "episode_03_goosebumps.mp4",
        "episode_04_hypnic_jerk.mp4", # Already archived in published_masters
    ]
    deleted_count = 0
    bytes_freed = 0
    for pat in remotion_purge:
        full_pat = os.path.join(REMOTION_DIR, pat)
        for match in glob.glob(full_pat):
            try:
                size = os.path.getsize(match)
                os.remove(match)
                deleted_count += 1
                bytes_freed += size
            except Exception as e:
                print(f"Failed to delete {match}: {e}")
                
    # Also clean temporary low-res test images in ep4 public folder
    ep4_purge = [
        "shot1_bed_falling_void.jpg",
        "shot6_jolt_awake_gasp_bed.jpg",
        "flux_test_bed.jpg",
        "test_pollinations.jpg",
        "test_turbo.jpg",
        "test_turbo.py",
        "test_flux_highres.py",
        "test_shot2_flux.py",
        "test_download.py",
    ]
    ep4_public = os.path.join(REMOTION_DIR, "public", "ep4")
    for f in ep4_purge:
        fp = os.path.join(ep4_public, f)
        if os.path.exists(fp):
            try:
                size = os.path.getsize(fp)
                os.remove(fp)
                deleted_count += 1
                bytes_freed += size
            except Exception as e:
                print(f"Failed to delete {fp}: {e}")

    mb_freed = bytes_freed / (1024 * 1024)
    print(f"\n[CLEANUP COMPLETE] Removed {deleted_count} temporary files, freeing {mb_freed:.2f} MB of disk space.")
    print(f"[PRESERVED] Masters in: {MASTERS_DIR}")
    print(f"[PRESERVED] Branding in: {BRANDING_DIR}")
    print(f"[PRESERVED] Remotion Engine in: {REMOTION_DIR}")
    print(f"[PRESERVED] Production Journal: {JOURNAL_FILE}")

if __name__ == "__main__":
    archive_and_clean()
