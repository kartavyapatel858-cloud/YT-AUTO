import { SceneConfig, SubtitleItem } from "../types";

export const EP3_SCENES: SceneConfig[] = [
  {
    id: "shot1_goosebumps_arm_shock",
    imageSrc: "ep3/shot1_goosebumps_arm_shock.jpg",
    durationInFrames: 258,
    effect: "camera_impact_shake",
    zoomStart: 1.0,
    zoomEnd: 1.09,
    panY: 0.01,
  },
  {
    id: "shot2_skin_cross_section_arrector",
    imageSrc: "ep3/shot2_skin_cross_section_arrector.jpg",
    durationInFrames: 207,
    effect: "camera_macro_zoom",
    zoomStart: 1.02,
    zoomEnd: 1.13,
    panY: 0.015,
  },
  {
    id: "shot3_sympathetic_nerve_adrenaline",
    imageSrc: "ep3/shot3_sympathetic_nerve_adrenaline.jpg",
    durationInFrames: 262,
    effect: "camera_macro_zoom",
    zoomStart: 1.0,
    zoomEnd: 1.12,
    panY: 0.01,
  },
  {
    id: "shot4_muscle_contraction_hair_upright",
    imageSrc: "ep3/shot4_muscle_contraction_hair_upright.jpg",
    durationInFrames: 195,
    effect: "camera_tension_pulse",
    zoomStart: 1.01,
    zoomEnd: 1.14,
    panY: 0.02,
  },
  {
    id: "shot5_prehistoric_fur_coat_fluff",
    imageSrc: "ep3/shot5_prehistoric_fur_coat_fluff.jpg",
    durationInFrames: 265,
    effect: "none",
    zoomStart: 1.02,
    zoomEnd: 1.10,
    panY: 0.01,
  },
  {
    id: "shot6_curious_character_smile",
    imageSrc: "ep3/shot6_curious_character_smile.jpg",
    durationInFrames: 202,
    effect: "none",
    zoomStart: 1.03,
    zoomEnd: 1.09,
    panY: 0.0,
  },
];

export const EP3_SUBTITLES: SubtitleItem[] = [
  {
    start: 0.1,
    end: 5.25,
    text: "Ever wonder why your skin suddenly breaks out in tiny bumps whenever you get terrified?",
  },
  {
    start: 5.25,
    end: 8.47,
    text: "That eerie reaction isn't just in your head.",
  },
  {
    start: 8.47,
    end: 15.16,
    text: "Deep under your skin, anchored to every single hair follicle, is a microscopic muscle called the arrector pili.",
  },
  {
    start: 15.16,
    end: 23.70,
    text: "When your brain senses sudden danger, your sympathetic nervous system fires an adrenaline surge, forcing these tiny muscles to violently contract!",
  },
  {
    start: 23.70,
    end: 30.01,
    text: "This contraction pulls the hair shaft completely upright and puckers the surrounding skin, creating a goosebump.",
  },
  {
    start: 30.01,
    end: 38.63,
    text: "Millions of years ago, when our ancestors were covered in thick fur, this fluffed up their coat to trap warm air and made them look twice as big to scare off predators.",
  },
  {
    start: 38.63,
    end: 45.31,
    text: "Today, we've lost the fur, but that prehistoric reflex remains frozen in your skin, leaving you to ask...",
  },
];
