import { useEffect, useState } from "react";
import { CRangeSlider } from '@coreui/react-pro'
import '@coreui/coreui-pro/dist/css/coreui.min.css';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import "./App.css";
import React from 'react'



const sampleRoute = {
  placements: [
    // increment for y is .115
    // increment for x is .007
    { x: 0.488, y: 0.245 },
    { x: 0.488, y: 0.36 },
    { x: 0.488, y: .303 },
    { x: .488, y: .418 },
    { x: .425, y: .418 },
    { x: .425, y: .303 }
  ],
};

// 🔹 Board Dimensions (match your actual image size)
const BOARD_SIZE = 800;  // Adjust to actual board width in pixels
const GRID_ROWS = 18;   // Number of rows
const GRID_COLS = 18;   // Number of columns
const SQUARE_SIZE = BOARD_SIZE / GRID_COLS; // Size of each square

// 🔹 Adjust these values if holds need shifting
const X_OFFSET = 30; // Shift right (+) or left (-)
const Y_OFFSET = 15; // Shift down (+) or up (-)
const SCALE_X = 0.95; // Fine-tune scaling
const SCALE_Y = 0.95; // Fine-tune scaling
const CIRCLE_RADIUS = 20; // Hold size

export function Board({route={}, size=BOARD_SIZE, activeSquares, setActiveSquares}) {

  
  const [holds, setHolds] = useState([]); // Holds for overlay circles

  // Fetch route from Flask server
  useEffect(() => {
    fetch("http://127.0.0.1:5000/generate_route", {
      method: "GET",
      headers: { "Content-Type": "application/json" }
    })
    .then((res) => res.json())
    .then((data) => {
      const normalizedHolds = data.map(hold => ({
        x: Math.round((hold.x * 9)) + .5,  // Scale `x` properly to grid index
        y: GRID_COLS - Math.round(hold.y * 9)  // Scale `y` properly to grid index
      }));
      
      const lowestYHold = normalizedHolds.reduce((min, normalizedHolds) => (normalizedHolds.y < min.y ? normalizedHolds : min), normalizedHolds[0]);
      // const lowestYHold = [...normalizedHolds].sort((a, b) => a.y - b.y)[0];
    
      {normalizedHolds.map((hold, index) => {
        const col = hold.x;
        const row = GRID_ROWS - hold.y;
        
        // const strokeColor = hold.y === lowestYHold.y ? "#ff00ff" : "#00ffff";
        const strokeColor = Math.abs(hold.y - lowestYHold.y) < 0.1 ? "#ff00ff" : "#00ffff";
        
        return (
          <g key={index}>
            <circle
              cx={col * SQUARE_SIZE + SQUARE_SIZE} // Align circles properly
              cy={row * SQUARE_SIZE + 0.5 * SQUARE_SIZE} // Use proper y-offset
              r={CIRCLE_RADIUS}
              stroke={strokeColor}
              strokeWidth="4"
              fill="transparent"
              style={{ cursor: "pointer" }}
            />
            <text
              x={col * SQUARE_SIZE + SQUARE_SIZE + 15} // Offset text for visibility
              y={row * SQUARE_SIZE + 0.5 * SQUARE_SIZE}
              fontSize="14"
              fill="white"
              fontWeight="bold"
              textAnchor="middle"
            >
              ({col}, {row})
            </text>
          </g>
        );
      })}
      

      setHolds(normalizedHolds);
    })
    .catch((err) => console.error("Error fetching route:", err));
  }, []);
  



  const lowestYHold = holds.reduce((min, holds) => (holds.y < min.y ? holds : min), holds[0]);

  const highestYHold = holds.reduce(
    (max, hold) => (hold.y > max.y ? hold : max), 
    holds[0]
  );

  const handleSquareClick = (row, col) => {

    
    const key = `${row}-${col}`;
    const selectedKeys = Object.keys(activeSquares).filter(k => activeSquares[k]);

    if (activeSquares[key]) {
      setActiveSquares((prev) =>({
        ...prev,
        [key]: !prev[key],
      }));
      return;
    }

    setActiveSquares((prev) =>({
      ...prev,
      [key]: !prev[key],
    }));

    const cx = col * SQUARE_SIZE + SQUARE_SIZE / 2;
    const cy = row * SQUARE_SIZE + SQUARE_SIZE / 2;
    setHolds((prevHolds) => {
      const exists = prevHolds.some((hold) => hold.x == cx && hold.y == cy)
      return exists ? prevHolds.filter((hold) => hold.x !== cx || hold.y !== cy) : [...prevHolds, {cx, cy}];
    });
  };

  return (
    <>
      {/* Climbing Board Image */}
      <img
        src="/10_9_combo.png"
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
        {Array.from({ length: GRID_ROWS }).map((_, row) =>
          Array.from({ length: GRID_COLS }).map((_, col) => {
            const key = `${row}-${col}`;
            if (col * SQUARE_SIZE + SQUARE_SIZE > BOARD_SIZE - 30) return null;

            if (activeSquares[key]) {
              // Render a green circle instead of a square
              return (
                <circle
                  key={key}
                  cx={col * SQUARE_SIZE + SQUARE_SIZE}
                  cy={row * SQUARE_SIZE + 0.5 * SQUARE_SIZE}
                  r={0.45 * SQUARE_SIZE}
                  fill="transparent"
                  stroke="#ffa500"
                  strokeWidth="5"
                  onClick={() => handleSquareClick(row, col)}
                  style={{ cursor: "pointer" }}
                />
              );
            } else {
              // Render a transparent square
              return (
                <rect
                  key={key}
                  x={col * SQUARE_SIZE + 0.5 * SQUARE_SIZE}
                  y={row * SQUARE_SIZE}
                  width={SQUARE_SIZE}
                  height={SQUARE_SIZE}
                  fill="transparent"
                  stroke="transparent"
                  strokeWidth="1"
                  onClick={() => handleSquareClick(row, col)}
                  style={{ cursor: "pointer" }}
                />
              );
            }
          })
      )}
       {/* Render fetched holds at correct positions */}
       {holds.map((hold, index) => {
          const col = hold.x;
          const row = hold.y;

          // Convert grid positions to actual pixel positions
          const cx = col * SQUARE_SIZE + SQUARE_SIZE / 2;
          const cy = row * SQUARE_SIZE + SQUARE_SIZE / 2;
          const strokeColor = Math.abs(hold.y - lowestYHold.y) < 0.1 ? "#ff00ff" : Math.abs(hold.y - highestYHold.y) < 0.1 ? "#00ff00" : "#00ffff";


          if (isNaN(cx) || isNaN(cy)) return (<></>);

          return (
            <g key={index}>
              <circle
                cx={cx}
                cy={cy}
                r={CIRCLE_RADIUS}
                stroke={strokeColor}
                strokeWidth="4"
                fill="transparent"
                style={{ cursor: "pointer" }}
              />
            </g>
          );
        })}
      </svg>
    </>
  );
}

export const submit = (activeSquares, sliderVal) => {
  for (const [key, val] of Object.entries(activeSquares)) {
    if(!val) continue
    const [row, col] = key.split("-").map(Number);
      
    activeSquares.push({ row, col });
  }

    console.log("Selected Squares:", activeSquares);
    console.log("Selected Slider Value:", sliderVal);

};

function App() {

  const [activeSquares, setActiveSquares] = useState({}); // Tracks clicked squares
  const [board, setBoard] = useState(
    <Board 
      route={[]}
      activeSquares={activeSquares}
      setActiveSquares={setActiveSquares}
    ></Board>
  );
  const [sliderVal, setSliderVal] = useState(0); 

  useEffect(() => {
    setBoard(
      <Board 
      route={[]}
      activeSquares={activeSquares}
      setActiveSquares={setActiveSquares}
    ></Board>
    )
  }, [activeSquares])

  return (
    <div className="container">
      <h1>KiltaBord</h1>
      <div className="board-container">
        {board}
      </div>
      <div className="generate-button">
        <Stack direction="row" spacing={2}>
        <div className="generate-button">
          <Stack direction="row" spacing={2}>
            <Button 
              variant="contained"
              color="success"
              onClick={() => submit(activeSquares, 0.25 * sliderVal)}
              className="generate-button"
            >
              Generate
            </Button>
          </Stack>
        </div>

        </Stack>
      </div>
    </div>
  );
}

export default App;
