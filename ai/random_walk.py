import weights
import numpy as np

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

    return ((index % len(a)) + x, (index // len(a)) + y)

x, y = 10, 10
print(next_hold(x, y, 10, False))