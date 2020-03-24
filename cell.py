import random


class Cell():

    def __init__(self, initial_rate, random_rate, initial_color=((255, 255, 255)), dead_color=((0, 0, 0))):
        self.state = True if random.random() < initial_rate else False
        self.initial_rate = initial_rate
        self.random_rate = random_rate
        self.initial_color = initial_color
        self.dead_color = dead_color
        self.color = initial_color if self.get_state() else dead_color
        self.neighbours = 0
        self.cluster = 0

    def get_state(self):
        return self.state

    def make_alive(self):
        self.color = self.initial_color
        self.state = True

    def make_dead(self):
        self.color = self.dead_color
        self.state = False

    def get_neighbors(self):
        return self.neighbours

    def set_neighbors(self, n):
        self.neighbours = n

    def get_cluster(self):
        return self.cluster

    def set_cluster(self, n):
        self.cluster = n

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def update_color(self):
        if self.get_state():  # defensive, should only be called by alive cells
            r_change = random.randint(-20, 20)
            g_change = random.randint(-20, 20)
            b_change = random.randint(-20, 20)

            color = self.get_color()

            r = color[0] + r_change if (color[0] + r_change <= 255
                                        and color[0] + r_change >= 0) else color[0]
            g = color[1] + g_change if (color[1] + g_change < 255
                                        and color[1] + g_change >= 0) else color[1]
            b = color[2] + b_change if (color[2] + b_change <= 255
                                        and color[2] + b_change >= 0) else color[2]

            self.set_color((r, g, b))

    def cluster_effect(self):
        if self.get_state():
            self.set_color((51, 255, 153))  # soft green
            # self.set_color((255, 153, 255))  # pink
            # self.set_color((51, 153, 255))  # light royal blue
            # self.set_color((0, 255, 0))  # GREEN
            # self.set_color((255, 255, 255))
            # self.set_color((0, 255, 128))
            # self.set_color((153, 255, 128))

    def __str__(self):
        if self.get_state():
            return "1"
        else:
            return "0"
