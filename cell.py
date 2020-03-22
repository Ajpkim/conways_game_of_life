import random


class Cell():

    def __init__(self, initial_rate, initial_color=((0, 255, 0)), dead_color=((0, 0, 0))):
        # self.initial_rate = initial_rate
        self.state = True if random.random() < initial_rate else False
        self.initial_color = initial_color
        self.dead_color = dead_color
        self.color = initial_color if self.state else dead_color
        self.neighbours = 0
        self.nearby = 0

    def get_state(self):
        return self.state

    def make_alive(self):
        self.state = True

    def make_dead(self):
        self.state = False

    def get_neighbors(self):
        return self.neighbours

    def set_neighbors(self, n):
        self.neighbours = n

    def get_nearby(self):
        return self.nearby

    def set_nearby(self, n):
        self.nearby = n

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def update_color(self):
        if self.get_state():  # precationary, should only be called by alive cells
            r_rate = random.randint(0, 20)
            g_rate = random.randint(0, 20)
            b_rate = random.randint(0, 20)

            color = self.get_color()

            r = color[0] + r_rate if color[0] + r_rate < 255 else color[0]
            g = color[0] + r_rate if color[1] + g_rate < 255 else color[1]
            b = color[0] + r_rate if color[2] + b_rate < 255 else color[2]

            self.set_color((r, g, b))

    def nearby_cluster(self, n):
        if self.nearby > n:
            self.set_color((0, 255, 255))

    def __str__(self):
        if self.get_state():
            return "1"
        else:
            return "0"

    # def __repr__(self):
    #     if self.get_state():
    #         print("1")
    #     else:
    #         print("0")
