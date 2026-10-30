import React from "react";
import {
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { CameraEffectType } from "../types";

interface Props {
  imageSrc: string;
  effect: CameraEffectType;
  zoomStart: number;
  zoomEnd: number;
  panX?: number;
  panY: number;
  rotation?: number;
}

export const ExplainerScene: React.FC<Props> = ({
  imageSrc,
  effect,
  zoomStart,
  zoomEnd,
  panX = 0,
  panY,
  rotation = 0,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  // 1. Primary Spring Physics for smooth organic camera motion (animation-principles)
  const spr = spring({
    frame,
    fps,
    config: {
      damping: 180,
      mass: 0.95,
      stiffness: 80,
    },
  });

  let zoom = interpolate(spr, [0, 1], [zoomStart, zoomEnd]);
  let translateX = interpolate(frame, [0, durationInFrames], [0, panX * 1080]);
  let translateY = interpolate(frame, [0, durationInFrames], [0, panY * 1920]);
  let rotateDeg = rotation;
  let brightness = 1.0;

  // 2. Subtle organic handheld camera micro-drift (eliminates robotic staticness)
  const t = frame / fps;
  const driftX = Math.sin(t * 1.3) * 6;
  const driftY = Math.cos(t * 1.1) * 7;
  translateX += driftX;
  translateY += driftY;

  // 3. Cinematic Camera Modes (Strictly Zero 2D Ripple Rings, Pure Camera Physics)

  // A. Falling Void / Vertigo: Downward camera plunge with subtle Dutch angle roll
  if (effect === "camera_drift_falling") {
    const fallProg = frame / durationInFrames;
    const accelFall = Math.pow(fallProg, 1.8) * 95;
    translateY += accelFall;
    rotateDeg += Math.sin(t * 1.6) * 1.3;
  }

  // B. Macro Zoom: Aggressive secondary push-in on biological landmark
  if (effect === "camera_macro_zoom") {
    const punchSpring = spring({
      frame: Math.max(0, frame - 12),
      fps,
      config: { damping: 140, mass: 0.8, stiffness: 95 },
    });
    zoom += interpolate(punchSpring, [0, 1], [0, 0.085]);
  }

  // C. Violent Impact Camera Shake (The Hypnic Jerk Jolt - beat-sync-editing & animation-principles)
  if (effect === "camera_impact_shake") {
    if (frame <= 48) {
      // Exponential decay envelope with natural physical dampening
      const hitProgress = frame / 48;
      const decay = Math.exp(-hitProgress * 5.2);
      const shakeX = Math.sin(frame * 2.3) * 38 * decay;
      const shakeY = Math.cos(frame * 2.7) * 34 * decay;
      const shakeRot = Math.sin(frame * 1.9) * 3.2 * decay;
      translateX += shakeX;
      translateY += shakeY;
      rotateDeg += shakeRot;
      zoom += 0.08 * decay;

      // High-speed optical sensor exposure burst on impact
      if (frame <= 5) {
        brightness = 1.0 + (1.0 - frame / 5) * 0.45;
      }
    }
  }

  // D. Tension Pulse: Subconscious biological heart rhythm breathing
  if (effect === "camera_tension_pulse") {
    const pulseCycle = Math.sin(t * Math.PI * 2 * 1.4);
    zoom += pulseCycle * 0.014;
  }

  // E. Sudden Recoil / Snap
  if (effect === "camera_recoil") {
    const snapSpring = spring({
      frame,
      fps,
      config: { damping: 90, mass: 0.5, stiffness: 180 },
    });
    translateX += interpolate(snapSpring, [0, 1], [28, 0]);
    zoom += interpolate(snapSpring, [0, 1], [0.07, 0]);
  }

  return (
    <div
      style={{
        position: "relative",
        width: 1080,
        height: 1920,
        overflow: "hidden",
        backgroundColor: "#020408",
      }}
    >
      {/* 3D Visual Master Layer with Pure Cinematic Camera Motion */}
      <div
        style={{
          width: "100%",
          height: "100%",
          transform: `scale(${zoom}) translate(${translateX}px, ${translateY}px) rotate(${rotateDeg}deg)`,
          transformOrigin: "center center",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          filter: `brightness(${brightness})`,
        }}
      >
        <Img
          src={staticFile(imageSrc)}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
          }}
        />
      </div>
    </div>
  );
};
