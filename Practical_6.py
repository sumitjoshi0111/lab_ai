
# Practical 6: 8 Queens using Backtracking

N = 8

# Check whether position is safe
def is_safe(board, row, col):

    for i in range(row):

        # Check same column or diagonal
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False

    return True


# Backtracking function
def solve(board, row):

    # All queens placed
    if row == N:
        return True

    for col in range(N):

        if is_safe(board, row, col):
            board[row] = col

            # Try next row
            if solve(board, row + 1):
                return True

            # Backtrack
            board[row] = -1

    return False


# Display chessboard
def print_board(board):

    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Main function
def main():

    board = [-1] * N

    if solve(board, 0):
        print("Solution Found!\n")
        print_board(board)
        print("Queen Positions:", board)
    else:
        print("No Solution Found")


if __name__ == "__main__":
    main()
