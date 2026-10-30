export type CameraEffectType =
  | "none"
  | "camera_drift_falling"
  | "camera_macro_zoom"
  | "camera_impact_shake"
  | "camera_tension_pulse"
  | "camera_recoil";

export interface SceneConfig {
  id: string;
  imageSrc: string;
  durationInFrames: number;
  effect: CameraEffectType;
  zoomStart: number;
  zoomEnd: number;
  panX?: number;
  panY: number;
  rotation?: number;
  sceneType?: "image" | "three_falling_void";
}

export interface SubtitleItem {
  start: number;
  end: number;
  text: string;
}
