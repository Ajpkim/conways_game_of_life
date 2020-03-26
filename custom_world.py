import random
import numpy as np
from cell import Cell


class CustomWorld():

    def __init__(self, state, initial_rate=.15, random_rate=0, size=(9, 9),
                 cluster_area=0, initial_color=(255, 255, 255), dead_color=(0, 0, 0,),
                 cluster_color=(51, 255, 153), color_rate=0):

        self.rows = len(state)
        self.cols = len(state[0])
        self.cell_grid = [[Cell(initial_rate, random_rate, size, initial_color, dead_color, cluster_color, color_rate)
                           for c in range(self.cols)] for r in range(self.rows)]
        self.world_state = state
        # self.world_state = [[1 if self.cell_grid[r][c].get_state() else 0 for c in range(cols)]
        #                     for r in range(rows)]
        self.cluster_area = cluster_area if cluster_area % 2 == 1 else cluster_area + 1
        self.set_world_state(state)

    def get_world_state(self):
        return self.world_state

    def set_world_state(self, state):
        assert len(state) == self.rows
        assert len(state[0]) == self.cols

        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cell_grid[row][col]

                if state[row][col] == 1:
                    cell.make_alive()
                else:
                    cell.make_dead()

        self.count_neighbors()
        self.count_cluster()
        self.update_world_state()

    def update_world_state(self):
        self.world_state = [[1 if self.cell_grid[r][c].get_state() else 0 for c in range(self.cols)]
                            for r in range(self.rows)]

    def update_world(self):
        # update every cell state based on current neighbours
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cell_grid[row][col]

                # logic for rules of game...
                if cell.get_state():
                    if cell.get_neighbors() < 2 or cell.get_neighbors() > 3:
                        cell.make_dead()
                    else:
                        if cell.color_rate > 0:  # possibly improve speed on larger inputs without color adj.
                            cell.update_color()
                else:
                    if cell.get_neighbors() == 3:
                        cell.make_alive()

                if random.random() < cell.random_rate:
                    cell.make_alive()
                    cell.set_color(cell.dead_color)
                    # cell.set_color((random.randint(0, 255),
                    #                 random.randint(0, 255), random.randint(0, 255)))

                if self.cluster_area >= 3:
                    self.cluster_effect(cell)

        # update cell properties after updating cell states
        self.count_neighbors()
        if self.cluster_area >= 3:
            self.count_cluster()
        self.update_world_state()

    def count_neighbors(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cell_grid[row][col]
                n = 0
                # look in 3x3 area with current cell in middle
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        # conditions for checking if [i,j] neighbor cell is valid location
                        if (row + i >= 0
                            and row + i < self.rows
                            and col + j >= 0
                            and col + j < self.cols
                                and not (i == 0 and j == 0)):  # don't count current cell as neighbor

                            if self.cell_grid[row + i][col + j].get_state():
                                n += 1
                cell.set_neighbors(n)

    def count_cluster(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cell_grid[row][col]
                n = 0

                for i in range(-(self.cluster_area // 2), self.cluster_area//2 + 1):
                    for j in range(-(self.cluster_area // 2), self.cluster_area//2 + 1):
                        # conditions for checking if [i,j] neighbor cell is valid location
                        if (row + i >= 0
                            and row + i < self.rows
                            and col + j >= 0
                            and col + j < self.cols
                                and not (i == 0 and j == 0)):

                            if self.cell_grid[row + i][col+j].get_state():
                                n += 1
                cell.set_cluster(n)

    def cluster_effect(self, cell):
        cluster_threshold = (self.cluster_area**2) // 3
        if cell.get_cluster() >= cluster_threshold:
            cell.cluster_effect()

    def __str__(self):
        s = ""
        for row in self.cell_grid:
            for i in range(0, len(row)):
                s = s + row[i].__str__() + " "
            s = s + "\n"
        return s
