import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def in_bounds(pos, grid_size):
    x, y = pos
    return 0 <= x < grid_size[0] and 0 <= y < grid_size[1]

def neighbors(pos, blocked, grid_size):
    x, y = pos
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if in_bounds((nx, ny), grid_size) and (nx, ny) not in blocked:
            yield (nx, ny)

def reconstruct_path(came_from, current, goal):
    path = [current]
    while current != goal:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def reverse_astar(goal, starts, blocked, grid_size):
    open_set = []
    heapq.heappush(open_set, (0, goal))

    came_from = {}
    g_score = {goal: 0}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current in starts:
            return current, reconstruct_path(came_from, current, goal)

        for neighbor in neighbors(current, blocked, grid_size):
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + min(heuristic(neighbor, s) for s in starts)
                heapq.heappush(open_set, (f, neighbor))

    return None, []
