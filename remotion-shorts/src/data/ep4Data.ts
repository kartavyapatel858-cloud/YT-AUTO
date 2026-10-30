import { SceneConfig, SubtitleItem } from "../types";

export const EP4_SCENES: SceneConfig[] = [
  // Shot 1: Man Sleeping in Bed & Drifting Off (Pixabay 2975x4510 3D Sleeping Reference)
  {
    id: "shot1_man_sleeping_bed",
    imageSrc: "ep4/shot1_bed_sleeping.png", // Ultra-sharp Pixabay asset: Man drifting off to sleep with spine exposed
    durationInFrames: 362, // 0 to 11.87s (356 frames + 6 transition)
    effect: "camera_drift_falling",
    zoomStart: 1.0,
    zoomEnd: 1.15,
    panY: 0.035,
    sceneType: "image",
  },
  // Shot 2: Sleep Paralysis Initiated (Pixabay 3D Holographic Head & Glowing Brainwave Locus)
  {
    id: "shot2_brain_sleep_switch",
    imageSrc: "ep4/shot2_brain_sleep_init.jpg", // 3D Wireframe Head, Glowing Thalamus Locus & Sinusoidal Brainwaves
    durationInFrames: 184, // 11.87s to 17.81s (178 frames + 6 transition)
    effect: "camera_macro_zoom",
    zoomStart: 1.02,
    zoomEnd: 1.16,
    panY: 0.015,
    sceneType: "image",
  },
  // Shot 3: Body & Muscle Dissolution (Pixabay 3072x5472 3D Medical Bust & Muscular Anatomy)
  {
    id: "shot3_muscle_fibers_limp",
    imageSrc: "ep4/shot3_muscles_relaxing.jpg", // 3D Medical CGI Bust with Thoracic Ribs, Cervical Spine & Facial Muscles
    durationInFrames: 157, // 17.81s to 22.83s (151 frames + 6 transition)
    effect: "camera_tension_pulse",
    zoomStart: 1.0,
    zoomEnd: 1.12,
    panY: 0.02,
    sceneType: "image",
  },
  // Shot 4: Brainstem Gravity Confusion / Internal Sensory Battle (Pixabay 3D Cerebral Synaptic Network)
  {
    id: "shot4_brainstem_falling_illusion",
    imageSrc: "ep4/shot4_brainstem_falling_battle.jpg", // 3D Cerebral Cortex & Intricate Branching Dendritic Network
    durationInFrames: 402, // 22.83s to 36.03s (396 frames + 6 transition)
    effect: "camera_drift_falling", // Vertigo falling plunge
    zoomStart: 1.04,
    zoomEnd: 1.22,
    panY: 0.045,
    sceneType: "image",
  },
  // Shot 5: THE EMERGENCY SHOCK & IMPACT SLAM (Pixabay 3840x2160 3D Transparent Body & Spinal Discharge)
  {
    id: "shot5_motor_cortex_emergency_shock",
    imageSrc: "ep4/shot5_spine_emergency_shock.jpg", // 3D Transparent Anatomical Body with Glowing Central Spinal Column & Radiating Plexus
    durationInFrames: 170, // 36.03s to 41.50s (164 frames + 6 transition)
    effect: "camera_impact_shake", // VIOLENT CAMERA RECOIL & EXPOSURE BURST ON IMPACT!
    zoomStart: 1.06,
    zoomEnd: 1.20,
    panY: 0.015,
    sceneType: "image",
  },
  // Shot 6: Snapping Back Awake to Reality (Pixabay 4148x2860 3D Startled Anatomical Bust Eyes Wide Open)
  {
    id: "shot6_jolt_awake_gasp_bed",
    imageSrc: "ep4/shot6_startled_awake_reality.jpg", // 3D Anatomical Bust with Wide Startled Eyes & Open Gasping Mouth
    durationInFrames: 157, // 41.50s to 46.73s (remaining frames)
    effect: "camera_recoil",
    zoomStart: 1.0,
    zoomEnd: 1.10,
    panY: 0.0,
    sceneType: "image",
  },
];

export const EP4_SUBTITLES: SubtitleItem[] = [
  {
    start: 0.1,
    end: 5.72,
    text: "Ever started drifting off to sleep, only to feel yourself falling and violently jerk awake?",
  },
  {
    start: 5.72,
    end: 11.87,
    text: "That terrifying jolt is called a hypnic jerk, and over seventy percent of all humans experience it.",
  },
  {
    start: 11.87,
    end: 17.81,
    text: "As you fall asleep, your brain initiates sleep paralysis so you don't physically act out your dreams.",
  },
  {
    start: 17.81,
    end: 22.83,
    text: "Your breathing slows, your brainwaves drop, and your muscles completely relax.",
  },
  {
    start: 22.83,
    end: 28.27,
    text: "But sometimes, your awake system and your sleep system battle for control during the handoff.",
  },
  {
    start: 28.27,
    end: 36.03,
    text: "When your muscles go limp too quickly, your confused brain stem misinterprets the sudden drop in tension as literally tumbling through mid-air!",
  },
  {
    start: 36.03,
    end: 41.50,
    text: "In a sheer panic to save your life, your motor cortex fires an explosive emergency shock straight down your spinal cord to catch yourself,",
  },
  {
    start: 41.50,
    end: 46.68,
    text: "violently snapping you back to reality before you ask...",
  },
];
