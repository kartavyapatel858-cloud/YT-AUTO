import React from "react";
import { useCurrentFrame, useVideoConfig, spring, interpolate } from "remotion";
import { SubtitleItem } from "../types";

interface Props {
  subtitles: SubtitleItem[];
}

export const KineticCaptions: React.FC<Props> = ({ subtitles }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const currentTime = frame / fps;

  // Find active subtitle cue block
  const currentSub = subtitles.find(
    (s) => currentTime >= s.start && currentTime <= s.end
  ) || (currentTime < subtitles[0]?.start ? subtitles[0] : null);

  if (!currentSub) {
    return null;
  }

  const words = currentSub.text.trim().split(/\s+/);
  if (words.length === 0) return null;

  const duration = Math.max(0.1, currentSub.end - currentSub.start);
  const relTime = Math.max(0, currentTime - currentSub.start);
  const progress = Math.min(1.0, relTime / duration);

  // Exact word index tracking
  const activeWordIdx = Math.min(
    words.length - 1,
    Math.floor(progress * words.length)
  );

  // Page into chunks of 3-4 words max (TikTok/Shorts retention standard)
  const chunkSize = words.length > 4 ? 4 : words.length;
  const chunkIndex = Math.floor(activeWordIdx / chunkSize);
  const startWord = chunkIndex * chunkSize;
  const endWord = Math.min(words.length, startWord + chunkSize);
  const displayWords = words.slice(startWord, endWord);
  const localActiveIdx = activeWordIdx - startWord;

  // Base frame for the active chunk
  const chunkStartSec = currentSub.start + (startWord / words.length) * duration;
  const chunkStartFrame = chunkStartSec * fps;

  return (
    <div
      style={{
        position: "absolute",
        top: 1380, // Universal 900x1400 safe area, clear of bottom 320px YouTube Shorts UI
        left: 0,
        width: 1080,
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        pointerEvents: "none",
        zIndex: 100,
      }}
    >
      <div
        style={{
          display: "inline-flex",
          flexWrap: "wrap",
          justifyContent: "center",
          alignItems: "center",
          gap: 12,
          maxWidth: 920,
          backgroundColor: "rgba(5, 8, 16, 0.82)",
          backdropFilter: "blur(14px)",
          border: "2px solid rgba(255, 255, 255, 0.18)",
          borderRadius: 24,
          padding: "16px 36px",
          boxShadow: "0 16px 40px rgba(0, 0, 0, 0.75)",
        }}
      >
        {displayWords.map((word, idx) => {
          const isActive = idx === localActiveIdx;
          const wordEnterFrame =
            chunkStartFrame + (idx / displayWords.length) * (duration / Math.ceil(words.length / chunkSize)) * fps;

          // Micro-overshoot spring physics per word from caption-animation skill
          const popSpring = spring({
            frame: Math.max(0, frame - wordEnterFrame),
            fps,
            config: { damping: 12, mass: 0.6 },
          });

          const wordScale = isActive
            ? interpolate(popSpring, [0, 1], [0.92, 1.10])
            : 1.0;

          return (
            <span
              key={idx}
              style={{
                fontFamily: "Impact, sans-serif",
                fontSize: 54,
                letterSpacing: 2.2,
                textTransform: "uppercase",
                color: isActive ? "#FFE600" : "#FFFFFF",
                WebkitTextStroke: "2.6px #000000",
                transform: `scale(${wordScale})`,
                margin: "0 8px", // Clean spacing so words never touch or merge
                display: "inline-block",
                filter: isActive
                  ? "drop-shadow(0 0 20px rgba(255, 230, 0, 0.85)) drop-shadow(0 4px 10px rgba(0, 0, 0, 0.95))"
                  : "drop-shadow(0 4px 8px rgba(0, 0, 0, 0.85))",
                transition: "color 0.08s ease, filter 0.08s ease",
              }}
            >
              {word}
            </span>
          );
        })}
      </div>
    </div>
  );
};
