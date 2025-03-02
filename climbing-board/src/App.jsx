import { useEffect, useState } from "react";
import "./App.css";

const sampleRoute = {
  placements: [
    // increment for y is .115
    // increment for x is .007
    { x: 0.488, y: 0.245 },
    { x: 0.488, y: 0.36 },
    { x: 0.488, y: .303 },
    { x: .488, y: .418 },
    { x: .425, y: .418 },
    { x: .418, y: .303 }
  ],
};

// 🔹 Board Dimensions (match your actual image size)
const BOARD_SIZE = 800;  // Adjust to actual board width in pixels

// 🔹 Adjust these values if holds need shifting
const X_OFFSET = 30; // Shift right (+) or left (-)
const Y_OFFSET = 15; // Shift down (+) or up (-)
const SCALE_X = 0.95; // Fine-tune scaling
const SCALE_Y = 0.95; // Fine-tune scaling
const CIRCLE_RADIUS = 20; // Hold size

export function Board({route, size=BOARD_SIZE}) {
  return (
    <>
      {/* Climbing Board Image */}
      <img
        src="/10_9_1.png"
        alt="Base Holds"
        className="board-image base"
      />

      {/* Overlay the holds using SVG */}
      <svg
        className="overlay"
        width={size}
        height={size}
        viewBox={`0 0 ${size} ${size}`}
      >
        {route.placements.map((hold, index) => (
          <circle
            key={index}
            cx={hold.x * size * SCALE_X + X_OFFSET}
            cy={hold.y * size * SCALE_Y + Y_OFFSET}
            r={CIRCLE_RADIUS}
            stroke="#00ffff"
            strokeWidth="4"
            fill="transparent"
            style={{ cursor: "pointer" }}
          />
        ))}
      </svg>
    </>
  )
}

function App() {
  const [board, setBoard] = useState(<Board route={sampleRoute}></Board>);

  return (
    <div className="container">
      <h1>KiltaBord</h1>
      <div className="board-container">
        {board}
      </div>
    </div>
  );
}

export default App;
