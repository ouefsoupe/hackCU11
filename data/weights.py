

import numpy as np

x = -1

weights = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, x, 3, x, 2, x, 3, x, 4, x, 4, x, 2, x, 4, x, 2, x, 4, x, 4, x, 4, x, 6, x, 4, x, 3, x, 3, x, 3, x],
    [7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x],
    [x, 3, x, 3, x, 4, x, 3, x, 2, x, 3, x, 3, x, 2, x, 4, x, 3, x, 3, x, 2, x, 3, x, 3, x, 2, x, 2, x, 5, x],
    
    [x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7],
    [x, 4, x, 3, x, 3, x, 3, x, 2, x, 3, x, 4, x, 1, x, 3, x, 2, x, 4, x, 3, x, 2, x, 2, x, 4, x, 3, x, 3, x],
    [7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x],
    [x, 3, x, 1, x, 2, x, 1, x, 2, x, 3, x, 2, x, 5, x, 2, x, 3, x, 3, x, 4, x, 3, x, 1, x, 2, x, 2, x, 1, x],
    
    [x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7],
    [x, 2, x, 2, x, 3, x, 2, x, 2, x, 1, x, 3, x, 3, x, 2, x, 3, x, 2, x, 2, x, 3, x, 3, x, 4, x, 4, x, 2, x],
    [7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x],
    [x, 2, x, 5, x, 2, x, 3, x, 4, x, 3, x, 2, x, 3, x, 3, x, 4, x, 3, x, 6, x, 2, x, 4, x, 2, x, 3, x, 6, x],
    
    [x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7],
    [x, 1, x, 2, x, 3, x, 2, x, 5, x, 4, x, 2, x, 3, x, 2, x, 3, x, 4, x, 5, x, 3, x, 3, x, 4, x, 3, x, 3, x],
    [7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x],
    [x, 3, x, 2, x, 4, x, 3, x, 3, x, 3, x, 2, x, 5, x, 4, x, 3, x, 3, x, 3, x, 4, x, 4, x, 3, x, 2, x, 3, x],
    
    [x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7],
    [x, 2, x, 4, x, 4, x, 3, x, 4, x, 3, x, 4, x, 3, x, 2, x, 3, x, 2, x, 3, x, 4, x, 2, x, 2, x, 5, x, 3, x],
    [7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x],
    [x, 2, x, 4, x, 2, x, 2, x, 2, x, 2, x, 3, x, 5, x, 3, x, 3, x, 4, x, 5, x, 3, x, 3, x, 1, x, 3, x, 2, x],
    
    [x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7],
    [x, 2, x, 3, x, 3, x, 3, x, 4, x, 3, x, 3, x, 3, x, 2, x, 4, x, 3, x, 5, x, 3, x, 5, x, 3, x, 3, x, 3, x],
    [7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x],
    [x, 4, x, 3, x, 2, x, 2, x, 3, x, 3, x, 4, x, 2, x, 5, x, 4, x, 4, x, 3, x, 2, x, 4, x, 4, x, 2, x, 3, x],
    
    [x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7],
    [x, 1, x, 3, x, 3, x, 2, x, 6, x, 3, x, 3, x, 3, x, 2, x, 3, x, 3, x, 3, x, 2, x, 4, x, 1, x, 3, x, 3, x],
    [7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x],
    [x, 2, x, 2, x, 3, x, 4, x, 3, x, 4, x, 3, x, 4, x, 3, x, 4, x, 4, x, 5, x, 4, x, 3, x, 3, x, 4, x, 4, x],
    
    [x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7],
    [x, 3, x, 3, x, 2, x, 1, x, 5, x, 4, x, 3, x, 3, x, 3, x, 4, x, 4, x, 6, x, 1, x, 3, x, 4, x, 3, x, 6, x],
    [7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x, x, 7, x, x],
    [x, 3, x, 3, x, 1, x, 2, x, 3, x, 2, x, 4, x, 7, x, 1, x, 2, x, 3, x, 2, x, 3, x, 4, x, 1, x, 4, x, 2, x],
    
    [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
    [x, 4, x, 3, x, 4, x, 3, x, 3, x, 3, x, 3, x, 4, x, 4, x, 3, x, 4, x, 3, x, 3, x, 6, x, 3, x, 3, x, 4, x],
    [x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x],
    [x, 2, x, 1, x, 3, x, 1, x, 1, x, 2, x, 1, x, 2, x, 1, x, 3, x, 2, x, 2, x, 2, x, 4, x, 3, x, 1, x, 2, x]])
    # top two rows of bolted holds each followed by empty rows

x, y = 1, 1
RADIUS = 3
X_MAX = weights.shape[1] - 1
Y_MAX = weights.shape[0] - 1
INF = 10

input_arr = np.ones(((RADIUS * 2) + 1, (RADIUS*2) + 1)) * INF
x1, x2 = x - RADIUS, x + RADIUS + 1
y1, y2 = y - RADIUS, y + RADIUS + 1

x1 = int(max(0, x1))
x2 = int(min(X_MAX, x2))
y1 = int(max(0, y1))
y2 = int(min(Y_MAX, y2))

input_arr[(y1-y + RADIUS):(y2-y + RADIUS), (x1 - x + RADIUS):(x2 - x + RADIUS)] = weights[y1:y2, x1:x2]
input_arr[RADIUS][RADIUS] = INF

print(input_arr)
model_input = input_arr.flatten()