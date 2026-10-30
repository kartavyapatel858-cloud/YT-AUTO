import json

transcript_path = r"D:\Youtube automation\remotion-shorts\public\ep6\transcript.json"
with open(transcript_path, "r", encoding="utf-8") as f:
    tdata = json.load(f)

scenes = [
    {
        "id": "shot1_numb_foot_hook",
        "imageSrc": "ep6/shot1_numb_foot_hook.png",
        "durationInFrames": 341,
        "effect": "camera_macro_zoom",
        "zoomStart": 1.0,
        "zoomEnd": 1.14,
        "panY": 0.02,
        "sceneType": "image"
    },
    {
        "id": "shot2_sciatic_nerve_anatomy",
        "imageSrc": "ep6/shot2_sciatic_nerve_anatomy.png",
        "durationInFrames": 323,
        "effect": "camera_tension_pulse",
        "zoomStart": 1.02,
        "zoomEnd": 1.15,
        "panY": 0.015,
        "sceneType": "image"
    },
    {
        "id": "shot3_compressed_nerve_ischemia",
        "imageSrc": "ep6/shot3_compressed_nerve_ischemia.png",
        "durationInFrames": 372,
        "effect": "camera_drift_falling",
        "zoomStart": 1.0,
        "zoomEnd": 1.12,
        "panY": 0.03,
        "sceneType": "image"
    },
    {
        "id": "shot4_oxygen_rush_release",
        "imageSrc": "ep6/shot4_oxygen_rush_release.png",
        "durationInFrames": 156,
        "effect": "camera_macro_zoom",
        "zoomStart": 1.03,
        "zoomEnd": 1.14,
        "panY": 0.02,
        "sceneType": "image"
    },
    {
        "id": "shot5_chaotic_neural_static_climax",
        "imageSrc": "ep6/shot5_chaotic_neural_static_climax.png",
        "durationInFrames": 198,
        "effect": "camera_impact_shake",
        "zoomStart": 1.06,
        "zoomEnd": 1.22,
        "panY": 0.015,
        "sceneType": "image"
    },
    {
        "id": "shot6_pins_needles_radiating",
        "imageSrc": "ep6/shot6_pins_needles_radiating.png",
        "durationInFrames": 274,
        "effect": "camera_recoil",
        "zoomStart": 1.0,
        "zoomEnd": 1.08,
        "panY": 0.0,
        "sceneType": "image"
    }
]

subtitles = []
for s in tdata["sentences"]:
    subtitles.append({
        "start": s["start"],
        "end": s["end"],
        "text": s["text"]
    })

ts_content = f"""import {{ SceneConfig, SubtitleItem }} from "../types";

export const EP6_SCENES: SceneConfig[] = {json.dumps(scenes, indent=2)};

export const EP6_SUBTITLES: SubtitleItem[] = {json.dumps(subtitles, indent=2)};
"""

target_path = r"D:\Youtube automation\remotion-shorts\src\data\ep6Data.ts"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(ts_content)

print(f"Created {target_path} successfully.")
