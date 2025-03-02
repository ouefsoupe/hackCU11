import weights
import numpy as np
from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import random


app = Flask(__name__)

CORS(app)
weight_matrix = weights.get_weights()

def getPossibleHolds(radius, x, y, weights, foot):
  X_MAX = weights.shape[1] - 1
  Y_MAX = weights.shape[0] - 1

  INF = np.inf

  input_arr = np.ones(((radius * 2) + 1, (radius*2) + 1)) * INF
  x1, x2 = x - radius, x + radius + 1
  y1, y2 = y - radius if foot else y, y if foot else y + radius + 1

  x1 = int(max(0, x1))
  x2 = int(min(X_MAX, x2))
  y1 = int(max(0, y1))
  y2 = int(min(Y_MAX, y2))
  input_arr[(y1-y + radius):(y2-y + radius), (x1 - x + radius):(x2 - x + radius)] = weights[y1:y2, x1:x2]
  input_arr[radius][radius] = INF
  return input_arr

def next_hold(x, y, difficulty, foot):
    global weight_matrix
    
    radius = 10
    a = getPossibleHolds(radius, x, y, weights=weight_matrix, foot=foot)

    a -= difficulty * 0.1

    a += np.random.random(size=(a.shape))
    a = np.abs(a)
    index = np.argmin(a)

    row = index // a.shape[1]
    col = index % a.shape[1]

    new_x = x + (col - radius)
    new_y = y + (row - radius) + 1

    return (new_x, new_y)

    # return ((index % len(a)) + x, (index // len(a)) + y)


def generate_sequence(start_x, start_y, difficulty, foot, num_moves):
    sequence = [(start_x, start_y)]
    
    x, y = start_x, start_y
    for _ in range(num_moves):
        x, y = next_hold(x, y, difficulty, foot)
        sequence.append((x, y))
        if(y == 18):
            break

    return sequence   


@app.route('/generate_route', methods=['GET'])
def get_route():
    GRID_WIDTH = 18
    GRID_HEIGHT = 18

    start_x = random.randint(0, GRID_WIDTH*2 - 3)
    start_y = random.randint(5, 9)
    num_moves = 7
    sequence = generate_sequence(start_x, start_y, difficulty=4, foot=False, num_moves=num_moves)

    response = [{"x": x / 18, "y": y / 18} for x, y in sequence]

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)


# x, y = 6, 9
# num_moves = 8
# sequence = generate_sequence(x, y, difficulty=10, foot=False, num_moves=num_moves)

# print("Sequential Holds Path:")
# for i, (x, y) in enumerate(sequence):
#     print(f"Move {i + 1}: ({x}, {y})")
