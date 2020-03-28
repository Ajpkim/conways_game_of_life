import pygame
from helper_functions import create_random_grid, get_state_from_file
import time
from custom_world import CustomWorld
from basic_world import BasicWorld


def run_random_classic_game(initial_rate, rows, cols, delay=0):
    random_state = create_random_grid(initial_rate, rows, cols)
    world = BasicWorld(random_state)
    game_loop(BasicWorld(random_state), delay)


def run_random_custom(rows=60, cols=60, initial_rate=0.15, random_rate=0, size=(9, 9),
                      cluster_area=0, initial_color=(255, 255, 255), dead_color=(0, 0, 0),
                      cluster_color=(51, 255, 153), color_rate=0, delay=0):
    state = create_random_grid(initial_rate, rows, cols)
    world = CustomWorld(state, initial_rate, random_rate, size, cluster_area,
                        initial_color, dead_color, cluster_color, color_rate)
    game_loop(world, delay)


def run_state_from_file_classic(filename, delay=0):
    state = get_state_from_file(filename)
    game_loop(BasicWorld(state), delay)


def run_state_from_file_custom(filename, initial_rate=0.15, random_rate=0, size=(9, 9),
                               cluster_area=0, initial_color=(255, 255, 255), dead_color=(0, 0, 0),
                               cluster_color=(51, 255, 153), color_rate=0, delay=0):
    state = get_state_from_file(filename)
    world = CustomWorld(state, initial_rate, random_rate, size, cluster_area,
                        initial_color, dead_color, cluster_color, color_rate)
    game_loop(world, delay)


def game_loop(world, delay=0):

    pygame.init()
    board = pygame.display.set_mode((world.cols*10, world.rows*10))

    pygame.display.set_caption("Conway's Game of Life")
    board.fill((0, 0, 0))

    pause = False
    run = True
    while run:
        # board.fill((0, 0, 0))  # need to uncomment if want to leave dead trails
        pygame.time.wait(delay)  # adjust delay if moving too fast
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
            # draw cells ... cell grid stored as [row][col] --> (y,x), so need to flip this for pygame --> (x, y)
            cell_image = pygame.Rect(col*10, row*10, cell.size[0], cell.size[1])
            pygame.draw.rect(board, cell.get_color(), cell_image)

    # #for troubleshooting
    # pygame.display.update()
    # pygame.time.wait(7500)
