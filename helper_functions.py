import random
import numpy as np


def create_random_grid(initial_rate, rows, cols):
    state = [[1 if random.random() < initial_rate else 0 for c in range(cols)]
             for r in range(rows)]
    return state


def get_state_from_file(filename):
    with open(filename, 'r') as f:
        state = np.genfromtxt(filename, delimiter=" ")
    return state
