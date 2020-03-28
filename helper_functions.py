import random
import numpy as np
import time
import timeit


def create_random_grid(initial_rate, rows, cols):
    state = [[1 if random.random() < initial_rate else 0 for c in range(cols)]
             for r in range(rows)]
    return state


def get_state_from_file(filename):
    state = []
    with open(filename, 'r') as f:
        for line in f:
            row = [int(x) for x in line.split(" ")]
            state.append(row)
    return state


# TESTING TIME
# print(timeit.timeit("""
# import numpy as np
# def get_state_from_file(filename):
#     with open(filename, 'r') as f:
#         state = np.genfromtxt(filename, delimiter=" ")
#     return state
# filename = "custom_states/mult_glider_generator_50x50.txt"
# state = get_state_from_file(filename)""", number=10000))
# ---> 27.69 seconds, 10,000 trials

# print(timeit.timeit("""def get_state_from_file(filename):
#     state = []
#     with open(filename, 'r') as f:
#         for line in f:
#             row = [int(x) for x in line.split(" ")]
#             state.append(row)
#     return state
# filename = "custom_states/mult_glider_generator_50x50.txt"
# state = get_state_from_file(filename)""", number=10000))
# ---> 8.091 seconds, 10,000 trials ... Way faster!
