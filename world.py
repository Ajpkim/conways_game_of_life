import numpy as np
from cell import Cell


class World():

    def __init__(self, rows, cols, initial_rate=0.3, cluster_area=5):
        # self.cell_grid = [[0 for i in range(rows)] for j in range(cols)]
        self.cell_grid = [[Cell(initial_rate) for c in range(cols)] for r in range(rows)]
        self.world_state = [[1 if self.cell_grid[r][c].get_state() else 0 for c in range(cols)]
                            for r in range(rows)]
        self.rows = rows
        self.cols = cols
        self.cluster_area = cluster_area if cluster_area % 2 == 1 else cluster_area + 1

        # make initalizing call to count_neighbors and count_cluster to intitalize cell properties
        self.count_neighbors()
        self.count_cluster(cluster_area)

    def get_world_state(self):
        return self.world_state

    def set_world_state(self):
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
                        cell.update_color()
                else:
                    if cell.get_neighbors() == 3:
                        cell.make_alive()

        # update cell properties after updating cell states
        self.count_neighbors()
        self.count_cluster(self.cluster_area)
        self.set_world_state()

        # # optional logic for cluster effects
        # for row in self.cell_grid:
        #     for col in self.cell_grid[row]:
        #         cell = self.cell_grid[row][col]
        #         cell.cluster_effect(5)

    def count_neighbors(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cell_grid[row][col]
                n = 0
                # look in 3x3 area with current cell in middle
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        # conditions for checking if [i,j] neighbor cell is valid
                        if (row + i >= 0
                            and row + i < self.rows
                            and col + j >= 0
                            and col + j < self.cols
                                and not (i == 0 and j == 0)):  # don't count current cell as neighbor

                            if self.cell_grid[row + i][col + j].get_state():
                                n += 1
                cell.set_neighbors(n)

    def count_cluster(self, area):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cell_grid[row][col]
                n = 0

                for i in range(-(self.cluster_area // 2), self.cluster_area//2 + 1):
                    for j in range(-(self.cluster_area // 2), self.cluster_area//2 + 1):
                        # conditions for checking if [i,j] neighbor cell is valid
                        if (row + i >= 0
                            and row + i < self.rows
                            and col + j >= 0
                            and col + j < self.cols
                                and not (i == 0 and j == 0)):

                            if self.cell_grid[row + i][col+j].get_state():
                                n += 1
                cell.set_cluster(n)

    def __str__(self):
        s = ""
        for row in self.cell_grid:
            for i in range(0, len(row)):
                s = s + row[i].__str__() + " "
            s = s + "\n"
        return s
