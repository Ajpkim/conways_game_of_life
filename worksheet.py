from cell import *
from world import *
from pygame_world import *

rows = 50
cols = 50
initial_rate = .2
cluster_area = 5
# w = World(rows, cols, initial_rate, cluster_area)
#
# board = Board(rows, cols)
# print(board.rows)

run_game(rows, cols, initial_rate, cluster_area)

# print(w)
#


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
