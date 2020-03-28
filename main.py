import numpy as np
import random
from custom_world import CustomWorld
from basic_world import BasicWorld
from cell import Cell
from run_pygame import *
from helper_functions import create_random_grid, get_state_from_file

# http://conwaylife.appspot.com/library

# ------------ CUSTOM ARGUMENTS ------------ #
rows = 50
cols = 50
initial_rate = .125
# random_rate = .00015
random_rate = 0
size = (9, 9)
cluster_area = 7
# initial_color = (51, 255, 153)
initial_color = (255, 255, 255)  # white
dead_color = (0, 0, 0)
# cluster_color = (255, 153, 255)  # bubblegum pink
cluster_color = (51, 255, 153)  # minty green
# cluster_color = (51, 153, 255)  # light royal blue
# cluster_color = (0, 255, 0)  # dark green
# cluster_color = (255, 255, 255)  # white
color_rate = 25
delay = 0

# ------------- SEED FILES ------------ #
filename = "custom_states/heart_beat.txt"
# filename = "custom_states/glider_generator_50x50.txt"
# filename = "custom_states/mult_glider_generator_50x50.txt"


# ---------- RUN GAME METHODS ------------ #


# #RANDOM W/ARGS
# run_random_custom(rows=rows, cols=cols, initial_rate=initial_rate, random_rate=random_rate, size=size,
#                   cluster_area=cluster_area, initial_color=initial_color, dead_color=dead_color,
#                   cluster_color=cluster_color, color_rate=color_rate, delay=delay)


# SEEDED W/ARGS
run_state_from_file_custom(filename=filename, initial_rate=initial_rate, random_rate=random_rate, size=size,
                           cluster_area=cluster_area, initial_color=initial_color, dead_color=dead_color,
                           cluster_color=cluster_color, color_rate=color_rate, delay=delay)


# #SEEDED CLASSIC
# run_state_from_file_classic(filename=filename, delay=delay)


# # SEEDED CUSTOM
# run_state_from_file_custom(filename=filename, initial_rate=0.15, random_rate=0, size=(9, 9),
#                            cluster_area=7, initial_color=(255, 255, 255), dead_color=(0, 0, 0),
#                            cluster_color=(51, 255, 153), color_rate=0, delay=0)


# #RANDOM CLASSIC
# run_random_classic_game(initial_rate=.1, rows=100, cols=100, delay=0)


# #RANDOM CUSTOM
# run_random_custom(rows=55, cols=55, initial_rate=.125, random_rate=.00015, size=(9, 9),
#                   cluster_area=7, initial_color=(255, 255, 255), dead_color=(0, 0, 0),
#                   cluster_color=(51, 255, 153), color_rate=20, delay=0)
