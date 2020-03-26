from cell import Cell


class BasicWorld():
    def __init__(self, state):
        self.rows = len(state)
        self.cols = len(state[0])
        self.cell_grid = [[Cell() for c in range(self.cols)] for r in range(self.rows)]
        self.set_world_state(state)

    def set_world_state(self, state):

        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cell_grid[row][col]

                if state[row][col] == 1:
                    cell.make_alive()
                else:
                    cell.make_dead()

        self.count_neighbors()

    def update_world(self):

        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cell_grid[row][col]

                # logic for rules of game...
                if cell.get_state():
                    if cell.get_neighbors() < 2 or cell.get_neighbors() > 3:
                        cell.make_dead()
                else:
                    if cell.get_neighbors() == 3:
                        cell.make_alive()

        self.count_neighbors()

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

    def __str__(self):
        s = ""
        for row in self.cell_grid:
            for i in range(0, len(row)):
                s = s + row[i].__str__() + " "
            s = s + "\n"
        return s
