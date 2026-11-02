
grid = [
    ['S', 0, 0],
    ['X', 0, 0],
    [0, 0, 'G']
]

# Initial Position
row = 0
col = 0

# Goal Position
goal = (2, 2)

# Internal State (Memory)
visited = []

print("Grid Navigation Begins\n")

while True:

    # Store visited location
    if (row, col) not in visited:
        visited.append((row, col))

    print("Current Position :", (row, col))
    print("Visited Cells :", visited)

    # Check Goal
    if (row, col) == goal:
        print("\nGoal Reached!")
        break

    moved = False

    # Move Right
    if col + 1 < 3 and grid[row][col + 1] != 'X' and (row, col + 1) not in visited:
        print("Action : Move Right")
        col += 1
        moved = True

    # Move Down
    elif row + 1 < 3 and grid[row + 1][col] != 'X' and (row + 1, col) not in visited:
        print("Action : Move Down")
        row += 1
        moved = True

    # Move Left
    elif col - 1 >= 0 and grid[row][col - 1] != 'X' and (row, col - 1) not in visited:
        print("Action : Move Left")
        col -= 1
        moved = True

    # Move Up
    elif row - 1 >= 0 and grid[row - 1][col] != 'X' and (row - 1, col) not in visited:
        print("Action : Move Up")
        row -= 1
        moved = True

    # No Valid Move
    if not moved:
        print("\nNo valid move available.")
        break

    print("-" * 40)

print("\nFinal Visited Cells :", visited)

print("\nRational Behaviour Analysis")
print("1. The agent stores previously visited cells.")
print("2. It avoids obstacles while navigating.")
print("3. It does not revisit explored locations.")
print("4. It uses its internal memory to decide the next move.")
print("Hence, it behaves as a Model-Based Intelligent Agent.")
