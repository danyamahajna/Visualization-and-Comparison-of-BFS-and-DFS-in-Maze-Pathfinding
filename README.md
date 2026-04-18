
# Maze Pathfinding Visualizer

This project demonstrates how search algorithms can be used to solve a maze navigation problem. It provides a visual representation of how an agent moves from a starting point to a goal while avoiding obstacles.

The application allows the user to run and compare two algorithms:
- Breadth-First Search (BFS)
- Depth-First Search (DFS)

## Purpose

The purpose of this project is to show how different search strategies behave when solving the same maze. It highlights the differences between BFS and DFS in terms of exploration, path quality, and performance.

## Features

- Interactive maze visualization
- BFS and DFS execution
- Step-by-step exploration display
- Highlighted final path
- Random maze generation
- Fixed maze reset option
- Performance metrics:
  - Number of visited cells
  - Path length
  - Execution time
- Status message indicating whether a path was found

## How It Works

The maze is represented as a grid where:
- Green cell = start
- Red cell = goal
- Purple cells = obstacles
- Yellow cells = explored nodes
- Blue cells = final path

The user can choose an algorithm, and the program visualizes how it explores the maze and reaches the goal.

## Algorithms Used

### Breadth-First Search (BFS)
- Explores the maze level by level
- Guarantees the shortest path
- Usually visits more cells

### Depth-First Search (DFS)
- Explores one path deeply before backtracking
- Does not guarantee the shortest path
- May reach the goal faster in some cases

## Project Structure

| File | Description |
|------|-------------|
| `main.py` | Handles the interface, buttons, visualization, and program flow |
| `maze.py` | Contains the maze representation, wall generation, and movement logic |
| `algorithms.py` | Implements BFS and DFS |
| `constants.py` | Stores colors, screen dimensions, and layout settings |

## Controls

- **Run BFS**: Executes Breadth-First Search
- **Run DFS**: Executes Depth-First Search
- **Reset**: Clears the current search result
- **New Maze**: Generates a random maze
- **Fixed Maze**: Restores the original maze layout

## Author

Danya Mahajna  
Istinye University

## How to Run

Make sure Python is installed.

Install pygame:

```bash
pip install pygame

## Run the Project


```bash
python3 main.py
