from collections import deque


def reconstruct_path(parent, start, goal):
    if goal != start and goal not in parent:
        return []

    path = [goal]
    current = goal

    while current != start:
        current = parent[current]
        path.append(current)

    path.reverse()
    return path


def bfs(maze):
    start = maze.start
    goal = maze.goal

    queue = deque([start])
    visited = {start}
    parent = {}
    visit_order = []

    while queue:
        current = queue.popleft()
        visit_order.append(current)

        if current == goal:
            return visit_order, reconstruct_path(parent, start, goal)

        for neighbor in maze.get_neighbors(*current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return visit_order, []


def dfs(maze):
    start = maze.start
    goal = maze.goal

    stack = [start]
    visited = {start}
    parent = {}
    visit_order = []

    while stack:
        current = stack.pop()
        visit_order.append(current)

        if current == goal:
            return visit_order, reconstruct_path(parent, start, goal)

        for neighbor in maze.get_neighbors(*current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)

    return visit_order, []