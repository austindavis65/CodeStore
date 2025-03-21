import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show(board):
    for row in range(3):
        print(f" {board[row * 3]} | {board[row * 3 + 1]} | {board[row * 3 + 2]} ")
        if row < 2:
            print("---+---+---")

def winner(board):

    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        return 'X'
    if board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        return 'X'
    if board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        return 'X'
    if board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        return 'X'
    if board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        return 'X'
    if board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        return 'X'
    if board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        return 'X'
    if board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        return 'X'

    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        return 'O'
    if board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        return 'O'
    if board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        return 'O'
    if board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        return 'O'
    if board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        return 'O'
    if board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        return 'O'
    if board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        return 'O'
    if board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        return 'O'
    return None

def play():
    board = [str(i) for i in range(9)]
    turn = "X"
    while any(cell.isdigit() for cell in board):
        clear_screen()
        print("Tic-Tac-Toe\n")
        show(board)
        print(f"\n{turn}'s turn!")
        try:
            move = int(input("Pick a spot (0-8): "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if 0 <= move < 9 and board[move].isdigit():
            board[move] = turn
            winner_result = winner(board)
            if winner_result:
                clear_screen()
                print("Tic-Tac-Toe\n")
                show(board)
                print(f"\n{winner_result} wins!")
                return
            turn = "O" if turn == "X" else "X"
        else:
            print("Spot is taken or out of range. Try again.")
    clear_screen()
    print("Tic-Tac-Toe\n")
    show(board)
    print("\nIt's a draw!")

play()
