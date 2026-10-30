import { SceneConfig, SubtitleItem } from "../types";

export const EP2_SCENES: SceneConfig[] = [
  {
    id: "shot1_shock",
    imageSrc: "ep2/shot1_brain_freeze_shock_1793333594656.jpg",
    durationInFrames: 239,
    effect: "camera_impact_shake",
    zoomStart: 1.0,
    zoomEnd: 1.09,
    panY: 0.02,
  },
  {
    id: "shot2_frost",
    imageSrc: "ep2/shot2_palate_cold_frost_1793333613139.jpg",
    durationInFrames: 199,
    effect: "camera_macro_zoom",
    zoomStart: 1.02,
    zoomEnd: 1.14,
    panY: 0.01,
  },
  {
    id: "shot3_artery",
    imageSrc: "ep2/shot3_artery_constriction_1793333632176.jpg",
    durationInFrames: 246,
    effect: "camera_tension_pulse",
    zoomStart: 1.0,
    zoomEnd: 1.11,
    panY: 0.02,
  },
  {
    id: "shot4_nerve",
    imageSrc: "ep2/shot4_trigeminal_nerve_pain_1793333653695.jpg",
    durationInFrames: 364,
    effect: "camera_macro_zoom",
    zoomStart: 1.0,
    zoomEnd: 1.12,
    panY: 0.01,
  },
  {
    id: "shot5_cure",
    imageSrc: "ep2/shot5_tongue_warmth_cure_v2_1793333699475.jpg",
    durationInFrames: 140,
    effect: "none",
    zoomStart: 1.02,
    zoomEnd: 1.12,
    panY: 0.015,
  },
  {
    id: "shot6_relief",
    imageSrc: "ep2/shot6_relief_thumbs_up_1793333722346.jpg",
    durationInFrames: 136,
    effect: "none",
    zoomStart: 1.03,
    zoomEnd: 1.11,
    panY: 0.0,
  },
];

export const EP2_SUBTITLES: SubtitleItem[] = [
  {
    start: 0.1,
    end: 3.5,
    text: "Ever drank an icy slushie and felt an ice pick stab your forehead?",
  },
  {
    start: 3.8,
    end: 7.78,
    text: "That agonizing headache isn't actually in your brain at all.",
  },
  {
    start: 7.9,
    end: 14.22,
    text: "When freezing liquid touches the warm roof of your mouth, your body panics.",
  },
  {
    start: 14.3,
    end: 22.23,
    text: "To protect your brain, your anterior cerebral artery rapidly constricts, then violently dilates to flood the area with warm blood.",
  },
  {
    start: 22.3,
    end: 28.5,
    text: "This sudden rush triggers your trigeminal nerve, the massive nerve responsible for facial sensation.",
  },
  {
    start: 28.6,
    end: 34.17,
    text: "Your brain misinterprets the distress signal as pain coming from your forehead—a phenomenon called referred pain!",
  },
  {
    start: 34.2,
    end: 38.65,
    text: "To stop it instantly, press your warm tongue flat against the roof of your mouth.",
  },
  {
    start: 38.7,
    end: 43.15,
    text: "This quickly reheats the tissue, silencing the alarm before you ask...",
  },
];
