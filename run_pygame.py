import pygame
import time
from world import World


def run_random_game(rows=50, cols=50, initial_rate=0.15, random_rate=0, size=(9, 9), cluster_area=0,
                    initial_color=(255, 255, 255), dead_color=(0, 0, 0,), cluster_color=(51, 255, 153), color_rate=0):
    # create world to animate
    world = World(rows, cols, initial_rate, random_rate, size, cluster_area,
                  initial_color, dead_color, cluster_color, color_rate)
    pygame.init()
    board = pygame.display.set_mode((rows*10, cols*10))
    pygame.display.set_caption("Conway's Game of Life")
    board.fill((0, 0, 0))

    pause = False
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                run = False

        animate_world(world, board)
        world.update_world()
        pygame.display.update()

    pygame.quit()


def run_custom_game(custom_state, rows=50, cols=50, initial_rate=0.15, random_rate=0,
                    size=(9, 9), cluster_area=0, initial_color=(255, 255, 255),
                    dead_color=(0, 0, 0,), cluster_color=(51, 255, 153), color_rate=0):

    world = World(rows, cols, initial_rate, random_rate, size, cluster_area,
                  initial_color, dead_color, cluster_color, color_rate)

    world.set_world_state(custom_state)

    pygame.init()
    board = pygame.display.set_mode((rows*10, cols*10))
    pygame.display.set_caption("Conway's Game of Life")
    board.fill((0, 0, 0))

    pause = False
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                run = False

        animate_world(world, board)
        world.update_world()
        pygame.display.update()

    pygame.quit()


def animate_world(world, board):
    for row in range(world.rows):
        for col in range(world.cols):
            cell = world.cell_grid[row][col]
            # draw cells
            cell_image = pygame.Rect(row*10, col*10, cell.size[0], cell.size[1])
            pygame.draw.rect(board, cell.get_color(), cell_image)


# def run_game_given_world(world):
#     pygame.init()
#     board = pygame.display.set_mode((world.rows*10, world.cols*10))
#     pygame.display.set_caption("Conway's Game of Life")
#     board.fill((0, 0, 0))
#
#     pause = False
#     run = True
#     while run:
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             if pygame.key.get_pressed()[pygame.K_SPACE]:
#                 run = False
#
#         animate_world(world, board)
#         world.update_world()
#         pygame.display.update()
#
#     pygame.quit()
