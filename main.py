import sys
import time
import pygame

from constants import *
from maze import Maze
from algorithms import bfs, dfs


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Pathfinding Visualizer")

font = pygame.font.SysFont(None, 30)
small_font = pygame.font.SysFont(None, 24)

maze = Maze()

current_algorithm = "None"
visited_count = 0
path_length = 0
execution_time = 0.0
status_message = "Ready"


BUTTON_WIDTH = 170
BUTTON_HEIGHT = 50
BUTTON_X = 720
BFS_BUTTON_Y = 100
DFS_BUTTON_Y = 170
RESET_BUTTON_Y = 240
NEW_MAZE_BUTTON_Y = 310
FIXED_MAZE_BUTTON_Y = 380


def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            x = GRID_OFFSET_X + col * CELL_SIZE
            y = GRID_OFFSET_Y + row * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            color = WHITE

            if maze.grid[row][col] == 1:
                color = PURPLE

            if (row, col) in maze.visited:
                color = YELLOW

            if (row, col) in maze.path:
                color = BLUE

            if (row, col) == maze.start:
                color = GREEN

            if (row, col) == maze.goal:
                color = RED

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)


def draw_button(x, y, text):
    rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, LIGHT_BLUE, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)

    label = font.render(text, True, BLACK)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)

    return rect


def draw_info():
    title = font.render("Maze Pathfinding Visualizer", True, BLACK)
    screen.blit(title, (650, 30))

    algo_text = small_font.render(f"Algorithm: {current_algorithm}", True, BLACK)
    visited_text = small_font.render(f"Visited cells: {visited_count}", True, BLACK)
    path_text = small_font.render(f"Path length: {path_length}", True, BLACK)
    time_text = small_font.render(f"Time: {execution_time:.2f} ms", True, BLACK)
    status_text = small_font.render(f"Status: {status_message}", True, BLACK)

    screen.blit(algo_text, (700, 470))
    screen.blit(visited_text, (700, 505))
    screen.blit(path_text, (700, 540))
    screen.blit(time_text, (700, 575))
    screen.blit(status_text, (700, 610))


def redraw_window():
    screen.fill(GRAY)

    bfs_button = draw_button(BUTTON_X, BFS_BUTTON_Y, "Run BFS")
    dfs_button = draw_button(BUTTON_X, DFS_BUTTON_Y, "Run DFS")
    reset_button = draw_button(BUTTON_X, RESET_BUTTON_Y, "Reset")
    new_maze_button = draw_button(BUTTON_X, NEW_MAZE_BUTTON_Y, "New Maze")
    fixed_maze_button = draw_button(BUTTON_X, FIXED_MAZE_BUTTON_Y, "Fixed Maze")

    draw_grid()
    draw_info()

    pygame.display.update()

    return bfs_button, dfs_button, reset_button, new_maze_button, fixed_maze_button


def animate_search(visit_order, path):
    global visited_count, path_length, status_message

    maze.reset_search()
    visited_count = 0
    path_length = 0

    for cell in visit_order:
        maze.visited.add(cell)
        visited_count = len(maze.visited)
        redraw_window()
        pygame.event.pump()
        pygame.time.delay(30)

    for cell in path:
        maze.path.append(cell)
        path_length = len(maze.path)
        redraw_window()
        pygame.event.pump()
        pygame.time.delay(50)

    if path:
        status_message = "Path found"
    else:
        status_message = "No path found"


def run_algorithm(algorithm_name):
    global current_algorithm, execution_time, status_message

    current_algorithm = algorithm_name
    status_message = "Searching..."

    if algorithm_name == "BFS":
        start_time = time.time()
        visit_order, path = bfs(maze)
        end_time = time.time()
    else:
        start_time = time.time()
        visit_order, path = dfs(maze)
        end_time = time.time()

    execution_time = (end_time - start_time) * 1000
    animate_search(visit_order, path)


def reset_stats():
    global current_algorithm, visited_count, path_length, execution_time, status_message
    current_algorithm = "None"
    visited_count = 0
    path_length = 0
    execution_time = 0.0
    status_message = "Ready"


def main():
    running = True

    while running:
        bfs_button, dfs_button, reset_button, new_maze_button, fixed_maze_button = redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if bfs_button.collidepoint(mouse_pos):
                    run_algorithm("BFS")

                elif dfs_button.collidepoint(mouse_pos):
                    run_algorithm("DFS")

                elif reset_button.collidepoint(mouse_pos):
                    maze.reset_search()
                    reset_stats()

                elif new_maze_button.collidepoint(mouse_pos):
                    maze.generate_random_maze()
                    reset_stats()

                elif fixed_maze_button.collidepoint(mouse_pos):
                    maze.create_fixed_walls()
                    reset_stats()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()