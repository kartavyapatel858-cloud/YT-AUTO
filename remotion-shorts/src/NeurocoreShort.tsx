import React from "react";
import { Audio, staticFile } from "remotion";
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { ExplainerScene } from "./components/ExplainerScene";
import { FallingVoidScene } from "./components/FallingVoidScene";
import { KineticCaptions } from "./components/KineticCaptions";
import { SceneConfig, SubtitleItem } from "./types";

export interface ShortProps extends Record<string, unknown> {
  scenes: SceneConfig[];
  subtitles: SubtitleItem[];
  audioSrc: string;
}

export const NeurocoreShort: React.FC<ShortProps> = ({
  scenes,
  subtitles,
  audioSrc,
}) => {
  return (
    <div
      style={{
        position: "relative",
        width: 1080,
        height: 1920,
        backgroundColor: "#000000",
        overflow: "hidden",
      }}
    >
      {/* Visual Scene Transitions */}
      <TransitionSeries>
        {scenes.map((scene, idx) => {
          return (
            <React.Fragment key={scene.id}>
              <TransitionSeries.Sequence durationInFrames={scene.durationInFrames}>
                {scene.sceneType === "three_falling_void" ? (
                  <FallingVoidScene />
                ) : (
                  <ExplainerScene
                    imageSrc={scene.imageSrc}
                    effect={scene.effect}
                    zoomStart={scene.zoomStart}
                    zoomEnd={scene.zoomEnd}
                    panY={scene.panY}
                  />
                )}
              </TransitionSeries.Sequence>
              {idx < scenes.length - 1 && (
                <TransitionSeries.Transition
                  presentation={fade()}
                  timing={linearTiming({ durationInFrames: 6 })}
                />
              )}
            </React.Fragment>
          );
        })}
      </TransitionSeries>

      {/* Kinetic Captions Layer */}
      <KineticCaptions subtitles={subtitles} />

      {/* Master Audio Track */}
      <Audio src={staticFile(audioSrc)} />
    </div>
  );
};
