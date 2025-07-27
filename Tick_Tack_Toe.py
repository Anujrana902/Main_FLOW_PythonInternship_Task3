def print_board(board):
    print('\n'.join(' '.join(row) for row in board))
    print()

def is_moves_left(board):
    return any(cell == '.' for row in board for cell in row)

def evaluate(board):
    # Check rows, cols, diagonals for wins
    lines = []
    lines.extend(board)
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2-i] for i in range(3)])
    for line in lines:
        if line == ['X']*3:
            return +10
        if line == ['O']*3:
            return -10
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = 'X'
                    val = minimax(board, depth+1, False)
                    board[i][j] = '.'
                    best = max(best, val)
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                    val = minimax(board, depth+1, True)
                    board[i][j] = '.'
                    best = min(best, val)
        return best

def find_best_move(board):
    best_val = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = '.'
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

def play_game():
    board = [['.' for _ in range(3)] for _ in range(3)]
    current_player = 'O'
    print("You: O  |  AI: X\n")
    while True:
        print_board(board)
        if current_player == 'O':
            r = int(input("Your row (0‑2): "))
            c = int(input("Your col (0‑2): "))
            if board[r][c] != '.':
                print("Invalid! Try again.")
                continue
            board[r][c] = 'O'
        else:
            r, c = find_best_move(board)
            board[r][c] = 'X'
            print(f"AI plays at {r},{c}")

        score = evaluate(board)
        if score == 10:
            print_board(board); print("AI wins!")
            break
        if score == -10:
            print_board(board); print("You win!")
            break
        if not is_moves_left(board):
            print_board(board); print("It's a tie!")
            break

        current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
    play_game()
