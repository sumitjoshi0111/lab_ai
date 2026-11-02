
# Tic-Tac-Toe using Minimax Algorithm

board = [" "] * 9

# Display Board
def display():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")


# Check Winner
def winner():
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None


# Minimax Algorithm
def minimax(is_max):
    result = winner()

    if result == "X":
        return 1
    if result == "O":
        return -1
    if " " not in board:
        return 0

    if is_max:
        best = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        best = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)

        return best


# AI Move
def ai_move():
    best_score = -100
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    if move != -1:
        board[move] = "X"


# Main Function
def main():
    print("Tic-Tac-Toe")
    print("You are O and AI is X")

    while True:
        display()

        # Human Move
        pos = int(input("Enter position (0-8): "))

        if pos < 0 or pos > 8 or board[pos] != " ":
            print("Invalid position!")
            continue

        board[pos] = "O"

        if winner() == "O":
            display()
            print("You Win!")
            break

        if " " not in board:
            display()
            print("Draw!")
            break

        # AI Move
        ai_move()

        if winner() == "X":
            display()
            print("AI Wins!")
            break

        if " " not in board:
            display()
            print("Draw!")
            break


if __name__ == "__main__":
    main()
