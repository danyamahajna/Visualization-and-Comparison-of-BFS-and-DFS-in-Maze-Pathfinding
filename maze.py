from constants import ROWS, COLS
import random


class Maze:
    def __init__(self):
        self.rows = ROWS
        self.cols = COLS

        self.start = (0, 0)
        self.goal = (ROWS - 1, COLS - 1)

        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.visited = set()
        self.path = []

        self.create_fixed_walls()

    def create_fixed_walls(self):
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        walls = [
            (0, 5), (1, 5), (2, 5), (3, 5), (4, 5),
            (4, 1), (4, 2), (4, 3), (4, 4),
            (2, 8), (3, 8), (4, 8), (5, 8), (6, 8),
            (6, 3), (6, 4), (6, 5), (6, 6), (6, 7),
            (8, 10), (9, 10), (10, 10), (11, 10),
            (10, 6), (10, 7), (10, 8), (10, 9),
            (12, 12), (13, 12), (14, 12), (15, 12),
            (15, 7), (15, 8), (15, 9), (15, 10), (15, 11),
            (17, 3), (17, 4), (17, 5), (17, 6),
            (7, 15), (8, 15), (9, 15), (10, 15), (11, 15),
            (13, 16), (14, 16), (15, 16), (16, 16)
        ]

        for row, col in walls:
            if (row, col) != self.start and (row, col) != self.goal:
                self.grid[row][col] = 1

        self.reset_search()

    def generate_random_maze(self, wall_probability=0.3):
        self.grid = []

        for row in range(self.rows):
            current_row = []
            for col in range(self.cols):
                if (row, col) == self.start or (row, col) == self.goal:
                    current_row.append(0)
                else:
                    current_row.append(1 if random.random() < wall_probability else 0)
            self.grid.append(current_row)

        self.reset_search()

    def reset_search(self):
        self.visited = set()
        self.path = []

    def is_valid_cell(self, row, col):
        return (
            0 <= row < self.rows
            and 0 <= col < self.cols
            and self.grid[row][col] == 0
        )

    def get_neighbors(self, row, col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if self.is_valid_cell(new_row, new_col):
                neighbors.append((new_row, new_col))

        return neighbors
