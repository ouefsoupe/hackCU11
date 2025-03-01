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
const BOARD_WIDTH = 800;  // Adjust to actual board width in pixels
const BOARD_HEIGHT = 800; // Adjust to actual board height in pixels

// 🔹 Adjust these values if holds need shifting
const X_OFFSET = 30; // Shift right (+) or left (-)
const Y_OFFSET = 15; // Shift down (+) or up (-)
const SCALE_X = 0.95; // Fine-tune scaling
const SCALE_Y = 0.95; // Fine-tune scaling
const CIRCLE_RADIUS = 20; // Hold size

function App() {
  const [route, setRoute] = useState(sampleRoute);

  return (
    <div className="container">
      <h1>KiltaBord</h1>
      <div className="board-container">
        {/* Climbing Board Image */}
        <img
          src="/10_9_1.png"
          alt="Base Holds"
          className="board-image base"
        />

        {/* Overlay the holds using SVG */}
        <svg
          className="overlay"
          width={BOARD_WIDTH}
          height={BOARD_HEIGHT}
          viewBox={`0 0 ${BOARD_WIDTH} ${BOARD_HEIGHT}`}
        >
          {route.placements.map((hold, index) => (
            <circle
              key={index}
              cx={hold.x * BOARD_WIDTH * SCALE_X + X_OFFSET}
              cy={hold.y * BOARD_HEIGHT * SCALE_Y + Y_OFFSET}
              r={CIRCLE_RADIUS}
              stroke="#00ffff"
              strokeWidth="4"
              fill="transparent"
              style={{ cursor: "pointer" }}
            />
          ))}
        </svg>
      </div>
    </div>
  );
}

export default App;
