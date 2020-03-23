import pygame
import time
from world import World


def run_game(rows, cols, initial_rate=0.3, cluster_area=5):
    # create world to animate
    world = World(rows, cols, initial_rate, cluster_area)

    pygame.init()
    board = pygame.display.set_mode((rows*10, cols*10))
    pygame.display.set_caption("Conway's Game of Life")
    board.fill((50, 50, 50))

    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            run = False

        animate_world(world, board)
        world.update_world()
        pygame.display.update()

    pygame.quit()


def animate_world(world, board):

    for row in range(world.rows):
        for col in range(world.cols):
            current_cell = world.cell_grid[row][col]
            cell_image = pygame.Rect(row*10, col*10, 10, 10)
            pygame.draw.rect(board, current_cell.get_color(), cell_image)
