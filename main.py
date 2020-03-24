import pygame
import sys
from world import World
from cell import Cell
from pygame_world import animate_world, run_game

rows = 50
cols = 50
initial_rate = .15
random_rate = .00015
initial_color = (255, 255, 255)
dead_color = (0, 0, 0)
cluster_color = (51, 255, 153)
cluster_area = 7
# run_game(rows, cols, initial_rate, random_rate, initial_color, dead_color,
#          cluster_color, cluster_area)

run_game(rows, cols)
