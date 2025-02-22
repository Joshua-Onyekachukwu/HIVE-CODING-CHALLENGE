# import the deque class from Python's collections module. double-ended queue

from collections import deque


def shortest_path(grid):
    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Check if the grid is empty or the start/end is blocked
    if rows == 0 or cols == 0 or grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1

    # Define the 4 possible movement directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initialize a queue for BFS
    queue = deque()
    queue.append((0, 0, 0))  # (row, col, distance)

    # Mark the start cell as visited
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = True

    # Perform BFS
    while queue:
        x, y, dist = queue.popleft()

        # Check if we've reached the destination
        if x == rows - 1 and y == cols - 1:
            return dist

        # Explore all 4 neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if the neighbor is within bounds, open, and unvisited
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    # If the destination is unreachable
    return -1


# Test case
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]


grid2 =[
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 1, 0]

]

print(shortest_path(grid))  # Output: 6

print(shortest_path(grid2))
