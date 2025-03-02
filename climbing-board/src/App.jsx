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

export function Board({size=BOARD_SIZE}) {

  const [activeSquares, setActiveSquares] = useState({}); // Tracks clicked squares
  const [holds, setHolds] = useState([]); // Holds for overlay circles
  


  // Fetch route from Flask server
  useEffect(() => {
    fetch("http://127.0.0.1:5000/generate_route", {
      method: "GET",
      headers: { "Content-Type": "application/json" }
    })
    .then((res) => res.json())
    .then((data) => {
      console.log("data: ", data)

      const normalizedHolds = data.map(hold => ({
        x: Math.round((hold.x* 8)),  // Scale `x` properly to grid index
        y: Math.round(hold.y * 8)   // Scale `y` properly to grid index
      }));
      console.log("Normalized Holds:", normalizedHolds);

      setHolds(normalizedHolds);
    })
    .catch((err) => console.error("Error fetching route:", err));
  }, []);
  


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

    if (selectedKeys.length >= 2) return;


    setActiveSquares((prev) =>({
      ...prev,
      [key]: !prev[key],
    }));

    const cx = col * SQUARE_SIZE + SQUARE_SIZE / 2;
    const cy = row * SQUARE_SIZE + SQUARE_SIZE / 2;

    setHolds((prevHolds) => {
      const exists = prevHolds.some((hold) => hold.cx == cx && hold.cy == cy)
      return exists ? prevHolds.filter((hold) => hold.cx !== cx || hold.cy !== cy) : [...prevHolds, {cx, cy}];
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
                  stroke="rgb(0, 255, 0)"
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
                  stroke="black"
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

          return (
            <g key={index}>
              <circle
                cx={cx}
                cy={cy}
                r={CIRCLE_RADIUS}
                stroke="#00ffff"
                strokeWidth="4"
                fill="transparent"
                style={{ cursor: "pointer" }}
              />
              {/* Render (x, y) text next to each hold */}
              <text
                x={cx + 20}  // Slight offset so text doesn't overlap
                y={cy}
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
      </svg>
    </>
  );
}
  

function App() {
  const [board, setBoard] = useState(<Board></Board>);

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
