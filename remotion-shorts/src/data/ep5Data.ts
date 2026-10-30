import { SceneConfig, SubtitleItem } from "../types";

export const EP5_SCENES: SceneConfig[] = [
  // Shot 1: The Hook - Young Man Cracking Knuckles
  {
    id: "shot1_cracking_hand",
    imageSrc: "ep5/shot1_cracking_hand.png",
    durationInFrames: 332, // 0.0s to 10.86s (326 frames + 6 transition)
    effect: "camera_macro_zoom",
    zoomStart: 1.0,
    zoomEnd: 1.14,
    panY: 0.02,
    sceneType: "image",
  },
  // Shot 2: Deep Anatomical Joint Cross-Section & Synovial Capsule
  {
    id: "shot2_joint_capsule_anatomy",
    imageSrc: "ep5/shot2_joint_capsule_anatomy.png",
    durationInFrames: 207, // 10.86s to 17.57s (201 frames + 6 transition)
    effect: "camera_tension_pulse",
    zoomStart: 1.02,
    zoomEnd: 1.15,
    panY: 0.015,
    sceneType: "image",
  },
  // Shot 3: Capsule Stretched Open Under Vacuum Negative Pressure
  {
    id: "shot3_vacuum_stretch",
    imageSrc: "ep5/shot3_vacuum_stretch.png",
    durationInFrames: 216, // 17.57s to 24.57s (210 frames + 6 transition)
    effect: "camera_drift_falling",
    zoomStart: 1.0,
    zoomEnd: 1.12,
    panY: 0.03,
    sceneType: "image",
  },
  // Shot 4: Nitrogen Gas Microscopic Nucleation & Cavitation Bubble
  {
    id: "shot4_cavitation_bubble_forms",
    imageSrc: "ep5/shot4_cavitation_bubble_forms.png",
    durationInFrames: 229, // 24.57s to 32.01s (223 frames + 6 transition)
    effect: "camera_macro_zoom",
    zoomStart: 1.04,
    zoomEnd: 1.20,
    panY: 0.02,
    sceneType: "image",
  },
  // Shot 5: CLIMAX - Violent Bubble Collapse & Acoustic Shockwave
  {
    id: "shot5_bubble_collapse_shockwave",
    imageSrc: "ep5/shot5_bubble_collapse_shockwave.png",
    durationInFrames: 310, // 32.01s to 42.12s (304 frames + 6 transition)
    effect: "camera_impact_shake", // Visceral camera recoil on shockwave impact at 36.0s!
    zoomStart: 1.06,
    zoomEnd: 1.22,
    panY: 0.015,
    sceneType: "image",
  },
  // Shot 6: Resolution - 60 Years Donald Unger Dual Hands Healthy Comparison
  {
    id: "shot6_healthy_hands_60years",
    imageSrc: "ep5/shot6_healthy_hands_60years.png",
    durationInFrames: 283, // 42.12s to 51.55s
    effect: "camera_recoil",
    zoomStart: 1.0,
    zoomEnd: 1.08,
    panY: 0.0,
    sceneType: "image",
  },
];

export const EP5_SUBTITLES: SubtitleItem[] = [
  {
    start: 0.1,
    end: 4.71,
    text: "What ACTUALLY makes that loud, satisfying crack when you pop your knuckles?",
  },
  {
    start: 4.66,
    end: 10.86,
    text: "Most people think bones are grinding together, or that this causes arthritis... but that's completely wrong.",
  },
  {
    start: 10.86,
    end: 17.57,
    text: "Inside your finger joints, two bones meet inside an airtight capsule filled with a slippery liquid called synovial fluid.",
  },
  {
    start: 17.57,
    end: 21.92,
    text: "When you pull or bend your finger, you force this capsule to stretch open.",
  },
  {
    start: 21.92,
    end: 24.57,
    text: "This creates an instant vacuum!",
  },
  {
    start: 24.57,
    end: 32.01,
    text: "Under this extreme negative pressure, dissolved nitrogen gas rapidly boils out of the fluid, forming a microscopic bubble.",
  },
  {
    start: 32.01,
    end: 39.22,
    text: "Within milliseconds, the surrounding fluid rushes back in, violently collapsing the bubble and firing an acoustic shockwave.",
  },
  {
    start: 39.22,
    end: 42.12,
    text: "That shockwave is the loud pop you hear!",
  },
  {
    start: 42.12,
    end: 44.31,
    text: "And as for arthritis?",
  },
  {
    start: 44.31,
    end: 48.54,
    text: "One doctor cracked only his left hand every day for sixty years.",
  },
  {
    start: 48.54,
    end: 51.55,
    text: "Both hands remained completely healthy!",
  },
];
