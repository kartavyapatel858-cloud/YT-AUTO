import { SceneConfig, SubtitleItem } from "../types";

export const EP6_SCENES: SceneConfig[] = [
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
];

export const EP6_SUBTITLES: SubtitleItem[] = [
  {
    "start": 0.1,
    "end": 5.271,
    "text": "Have you ever sat on your foot, stood up, and felt like your leg was made of dead rubber?"
  },
  {
    "start": 5.221,
    "end": 11.164,
    "text": "Then, seconds later, an intense burning prickle rushes in like thousands of tiny electric needles!"
  },
  {
    "start": 11.164,
    "end": 16.042,
    "text": "Most people think you cut off blood circulation... but that's actually a myth."
  },
  {
    "start": 16.042,
    "end": 21.74,
    "text": "Running through your leg are major nerve bundles packed with thousands of microscopic sensory fibers."
  },
  {
    "start": 21.74,
    "end": 25.956,
    "text": "When you sit awkwardly, you physically crush this nerve against bone."
  },
  {
    "start": 25.956,
    "end": 31.924,
    "text": "This compression starves the nerve fibers of oxygen, choking off the electrical signals to your brain."
  },
  {
    "start": 31.924,
    "end": 33.934,
    "text": "Your foot goes numb."
  },
  {
    "start": 33.934,
    "end": 38.922,
    "text": "When you finally stand up and release the pressure, oxygen suddenly floods back in!"
  },
  {
    "start": 38.922,
    "end": 45.319,
    "text": "As the starved neurons reboot, they fire wildly and uncontrollably like chaotic static electricity!"
  },
  {
    "start": 45.319,
    "end": 54.449,
    "text": "Your brain can't decode this sudden avalanche of random signals, so it translates the chaos as that sharp, prickly burning sensation until the nerve pathway stabilizes!"
  }
];
