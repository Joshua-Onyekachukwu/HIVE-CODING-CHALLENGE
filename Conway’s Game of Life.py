def game_of_life(board):
    # Get the dimensions of the board
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    # Create a copy of the board to store the next state
    next_board = [[0 for _ in range(cols)] for _ in range(rows)]

    # Define the 8 possible neighbor directions
    directions = [(-1, -1), (-1, 0), (-1, 1),  (0, -1),
                  (0, 1),   (1, -1), (1, 0),   (1, 1)]

    # Iterate through each cell in the board
    for i in range(rows):
        for j in range(cols):
            # Count the live neighbors
            live_neighbors = 0
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < rows and 0 <= y < cols and board[x][y] == 1:
                    live_neighbors += 1

            # Apply the rules of the Game of Life
            if board[i][j] == 1:  # Cell is alive
                if live_neighbors < 2 or live_neighbors > 3:
                    next_board[i][j] = 0  # Dies
                else:
                    next_board[i][j] = 1  # Survives
            else:  # Cell is dead
                if live_neighbors == 3:
                    next_board[i][j] = 1  # Becomes alive

    return next_board


# Test case
board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
]


next_generation = game_of_life(board)
for row in next_generation:
    print(row)