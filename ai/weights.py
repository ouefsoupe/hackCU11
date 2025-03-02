import numpy as np

def get_weights():
    x = -1
    return np.array([
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
