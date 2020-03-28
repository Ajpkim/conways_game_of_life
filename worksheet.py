import numpy as np
from cell import *
from basic_world import BasicWorld
from custom_world import CustomWorld
from run_pygame import *
from helper_functions import *

# help(pygame.display)
filename = "custom_states/testing_get_state.txt"
state = get_state_from_file(filename)

world = BasicWorld(state)

board = pygame.display.set_mode((world.cols*10, world.rows*10))

animate_world(world, board)

for row in range(world.rows):
    print([cell.__str__() for cell in world.cell_grid[row]])


# print('state...')
# for row in state:
#     print(row)
#
#
# print("")
#
#
# print('cell grid...')
# for row in range(bw.rows):
#
#     print([cell.__str__() for cell in bw.cell_grid[row]])
#
# print("")
# print('updating...')
# bw.update_world()
# print('updated cell grid...')
# for row in range(bw.rows):
#
#     print([cell.__str__() for cell in bw.cell_grid[row]])


# row = ['1' if cell.get_state() else 0 for cell in bw.cell_grid[row]]
# print(row)
# print(bw)

# print('cell gird', bw.cell_grid)


# filename = "custom_states/testing_get_state.txt"
# bw = BasicWorld(filename)
# print(bw)

# fw = BasicWorld(custom_state=[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])
# print(fw)
# fw.update_world()
# print(fw)
# game_loop(fw)

# def get_state_from_file(filename):
#     with open(filename, 'r') as f:
#         state = np.genfromtxt(filename, delimiter=",")
#     return data
#
#
# filename = "custom_states/10x10_template.txt"
#
# custom_state = get_state_from_file(filename)
# print(custom_state)
# run_classic_game(.15, 65, 65)

# cw = CustomWorld(create_random_grid(.5, 10, 10))
# print(cw)

# cw = CustomWorld()

# for i in range(len(data)):
#     for j in range(len(data)):
#         data[i][j] = int


# rows = 50
# cols = 50
# initial_rate = .15
# # initial_color = (255, 255, 255)
# # dead_color = (0, 0, 0)
# random_rate = .00015
# # cluster_effects = True
# # cluster_area = 7
# # run_game(rows, cols, initial_rate, random_rate,)
# run_game(rows, cols)


# print(w)
#


# w = World(rows, cols, initial_rate, cluster_area)
#
# board = Board(rows, cols)
# print(board.rows)
#
# def neighbors_grid(w):
#     print("neighbor's grid:")
#     s = ""
#     for row in w.grid:
#         for i in range(0, len(row)):
#             s = s + str(row[i].get_neighbors()) + " "
#         s = s + "\n"
#     print(s)
#
#
# neighbors_grid(w)
# print('updating world...')
# w.update_world()
# print(w)
# neighbors_grid(w)


# -------------Testing count_neighbors---------------
# def neighbors_grid(w):
#     print("neighbor's grid:")
#     s = ""
#     for row in w.grid:
#         for i in range(0, len(row)):
#             s = s + str(row[i].get_neighbors()) + " "
#         s = s + "\n"
#     print(s)


# w.count_neighbors()
# print("neighbors grid count:")
# s = ""
# for row in w.grid:
#     for i in range(0, len(row)):
#         s = s + str(row[i].get_neighbors()) + " "
#     s = s + "\n"
# print(s)
#
# print("\n\n\n")
# # print("cluster_area = ", w.cluster_area)
#
# w.count_neighbors()
# print("neighbors grid count:")
# s = ""
# for row in w.grid:
#     for i in range(0, len(row)):
#         s = s + str(row[i].get_neighbors()) + " "
#     s = s + "\n"
# print(s)
#
# print("\n\n\n")
# print("cluster_area = ", w.cluster_area)


#


# a = [[0, 10], [1, 11], [2, 12]]
# print(a[-1][1])


# print(a[3][3])

# ### update_world test
# print(w)
# print("\n\n")
# w.update_world()
#
# print(w)


# print(w.grid)

# for row in w.grid:
#     r = []
#     for i in range(0, len(row)):
#         r.append(row[i].__str__())
#     print(r)

# c = Cell(1)
#
# print(c.get_state())


# alive = 0
# for i in range(0, 10000):
#     c = Cell(.1)
#     if c.state:
#         alive += 1
#
# print(alive)

# rows, cols = 5, 5
# a = [[0 for i in range(rows)] for j in range(cols)]
# print(a)
#
# a[3][0] = 33
# print(a)
#
# if a[3][0] > 50 or a[3][0] > 51:
#     print("works")

# print(9 // 2)
