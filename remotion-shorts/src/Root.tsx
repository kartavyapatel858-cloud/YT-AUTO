import React from "react";
import { Composition } from "remotion";
import { NeurocoreShort } from "./NeurocoreShort";
import { FallingVoidScene } from "./components/FallingVoidScene";
import { EP2_SCENES, EP2_SUBTITLES } from "./data/ep2Data";
import { EP3_SCENES, EP3_SUBTITLES } from "./data/ep3Data";
import { EP4_SCENES, EP4_SUBTITLES } from "./data/ep4Data";
import { EP5_SCENES, EP5_SUBTITLES } from "./data/ep5Data";
import { EP6_SCENES, EP6_SUBTITLES } from "./data/ep6Data";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition<any, any>
        id="Episode06-PinsAndNeedles"
        component={NeurocoreShort}
        durationInFrames={1634}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          scenes: EP6_SCENES,
          subtitles: EP6_SUBTITLES,
          audioSrc: "ep6/audio.m4a",
        }}
      />
      <Composition<any, any>
        id="Episode05-KnuckleCrack"
        component={NeurocoreShort}
        durationInFrames={1547}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          scenes: EP5_SCENES,
          subtitles: EP5_SUBTITLES,
          audioSrc: "ep5/audio.m4a",
        }}
      />
      <Composition
        id="FallingVoidTest"
        component={FallingVoidScene}
        durationInFrames={360}
        fps={30}
        width={1080}
        height={1920}
      />
      <Composition<any, any>
        id="Episode04-HypnicJerk"
        component={NeurocoreShort}
        durationInFrames={1402}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          scenes: EP4_SCENES,
          subtitles: EP4_SUBTITLES,
          audioSrc: "ep4/audio.m4a",
        }}
      />
      <Composition<any, any>
        id="Episode03-Goosebumps"
        component={NeurocoreShort}
        durationInFrames={1359}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          scenes: EP3_SCENES,
          subtitles: EP3_SUBTITLES,
          audioSrc: "ep3/audio.m4a",
        }}
      />
      <Composition<any, any>
        id="Episode02-BrainFreeze"
        component={NeurocoreShort}
        durationInFrames={1294}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          scenes: EP2_SCENES,
          subtitles: EP2_SUBTITLES,
          audioSrc: "ep2/audio.m4a",
        }}
      />
    </>
  );
};
