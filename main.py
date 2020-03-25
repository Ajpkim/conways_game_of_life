import numpy as np
from world import World
from cell import Cell
from run_pygame import animate_world, run_random_game, run_custom_game

rows = 50
cols = 50
initial_rate = .125
random_rate = .00015
size = (9, 9)
cluster_area = 7
initial_color = (255, 255, 255)
dead_color = (0, 0, 0)
cluster_color = (51, 255, 153)
color_rate = 20
filename = "custom_states/second_state_50x50.txt"


# CHECK HOW CUSTOM STATE IS BUILT MEANING ROWS VS COLS... IS IT AS EXPECTED OR OPPOSITE

def get_state_from_file(filename):
    with open(filename, 'r') as f:
        state = np.genfromtxt(filename, delimiter=" ")
    return state


# # RUN CUSTOM GAME WITH STATE FROM TXT FILE
custom_state = get_state_from_file(filename)
run_custom_game(custom_state, rows=len(custom_state), cols=len(custom_state[0]), initial_rate=0, random_rate=0, size=(9, 9),
                cluster_area=7, initial_color=(255, 255, 255), dead_color=(0, 0, 0), cluster_color=(51, 255, 153), color_rate=20)

# ----------------- SOME BASIC PRESETS ------------------- #
# # RUN WITH ABOVE ARGS
# run_random_game(rows, cols, initial_rate, random_rate, size, cluster_area, initial_color, dead_color,
#                 cluster_color, color_rate)

# #BASIC GAME VERSION
# run_random_game(rows=50, cols=50, initial_rate=.15, random_rate=0, initial_color=(0, 185, 80),
# cluster_area = 0, color_rate = 0)

# # BASIC WHITE/BLACK VERSION
# run_random_game()

# #PREFERRED DEFAULT WITH CLUSTERING
# run_random_game(rows=50, cols=50, initial_rate=.15, cluster_area=7)

# #PREFERRED DEFAULT WITH CLUSTERING, RANDOMNESS
# run_random_game(rows=50, cols=50, initial_rate=.125, random_rate=.00015, cluster_area=7)

# #PREFERRED DEFAULT CLUSTERING, RANDOMNESS, COLORING
# run_random_game(rows=50, cols=50, initial_rate=.125,
#                 random_rate=.00015, cluster_area=7, color_rate=25)
