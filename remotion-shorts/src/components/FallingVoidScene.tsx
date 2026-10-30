import React, { useMemo } from "react";
import { ThreeCanvas } from "@remotion/three";
import { useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import * as THREE from "three";

// 3D Particles Field (Starfield / Void Dust)
const VoidParticles: React.FC<{ count: number; frame: number }> = ({ count, frame }) => {
  const points = useMemo(() => {
    const coords = new Float32Array(count * 3);
    for (let i = 0; i < count; i++) {
      coords[i * 3] = (Math.sin(i * 99) * 2 - 1) * 16;
      coords[i * 3 + 1] = ((Math.cos(i * 33) * 2 - 1) * 25);
      coords[i * 3 + 2] = (Math.sin(i * 77) * 2 - 1) * 16;
    }
    return coords;
  }, [count]);

  // Translate particles upwards to simulate camera falling downward
  const offsetPositions = useMemo(() => {
    const updated = new Float32Array(points.length);
    for (let i = 0; i < count; i++) {
      updated[i * 3] = points[i * 3];
      // upward drift loop
      const origY = points[i * 3 + 1];
      updated[i * 3 + 1] = ((origY + frame * 0.25 + 25) % 50) - 25;
      updated[i * 3 + 2] = points[i * 3 + 2];
    }
    return updated;
  }, [points, count, frame]);

  return (
    <points>
      <bufferGeometry>
        <bufferAttribute
          attach="attributes-position"
          args={[offsetPositions, 3]}
        />
      </bufferGeometry>
      <pointsMaterial
        size={0.14}
        color="#00f0ff"
        transparent
        opacity={0.8}
        blending={THREE.AdditiveBlending}
      />
    </points>
  );
};

// 3D Procedural Falling Void Scene
export const FallingVoidScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { width, height } = useVideoConfig();

  // Dynamic Camera Vertigo Plunge Physics
  const fallProgress = frame / 190;
  const cameraY = interpolate(fallProgress, [0, 1], [3.5, -4.5]);
  const cameraZ = interpolate(fallProgress, [0, 1], [7.5, 4.2]);
  const bedTilt = interpolate(fallProgress, [0, 1], [0.15, -0.35]);
  const bedRoll = Math.sin(frame * 0.05) * 0.12;

  return (
    <div style={{ width, height, backgroundColor: "#02040b" }}>
      <ThreeCanvas
        width={width}
        height={height}
        camera={{ position: [0, cameraY, cameraZ], fov: 55 }}
      >
        <ambientLight intensity={0.7} />
        {/* Cinematic Rim Lights */}
        <pointLight position={[6, cameraY + 4, 5]} intensity={3.5} color="#00e5ff" />
        <pointLight position={[-6, cameraY - 2, 3]} intensity={2.8} color="#ff3366" />
        <directionalLight position={[0, 10, 5]} intensity={1.2} color="#ffffff" />

        {/* 3D Floating Bed Tumbling into Void */}
        <group position={[0, 0, 0]} rotation={[bedTilt, 0.4 + bedRoll, bedRoll]}>
          {/* Bed Base Frame */}
          <mesh position={[0, -0.35, 0]}>
            <boxGeometry args={[3.2, 0.3, 5.8]} />
            <meshStandardMaterial color="#0d1527" roughness={0.3} metalness={0.7} />
          </mesh>

          {/* Mattress */}
          <mesh position={[0, 0, 0]}>
            <boxGeometry args={[3.0, 0.5, 5.5]} />
            <meshStandardMaterial color="#1e293b" roughness={0.6} />
          </mesh>

          {/* Pillow */}
          <mesh position={[0, 0.38, -2.0]}>
            <boxGeometry args={[2.0, 0.28, 1.0]} />
            <meshStandardMaterial color="#38bdf8" roughness={0.5} emissive="#0284c7" emissiveIntensity={0.2} />
          </mesh>

          {/* Blanket / Body Form */}
          <mesh position={[0, 0.32, 0.4]}>
            <boxGeometry args={[2.6, 0.4, 3.8]} />
            <meshStandardMaterial color="#0f172a" roughness={0.7} />
          </mesh>

          {/* 3D Stylized Head */}
          <mesh position={[0, 0.58, -1.9]}>
            <sphereGeometry args={[0.48, 32, 32]} />
            <meshStandardMaterial color="#fcd34d" roughness={0.4} emissive="#f59e0b" emissiveIntensity={0.15} />
          </mesh>
        </group>

        {/* 3D Dynamic Void Particles Tunnel */}
        <VoidParticles count={400} frame={frame} />

        {/* Falling Spatial Grid Planes */}
        <gridHelper args={[30, 30, "#00f0ff", "#1e1b4b"]} position={[0, -5, 0]} />
      </ThreeCanvas>
    </div>
  );
};
