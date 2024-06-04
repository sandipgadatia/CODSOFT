
from .board import print_board, check_winner, is_board_full
from .minimax import find_best_move

def human_move(board):
    while True:
        row, col = map(int, input("Enter your move (row and column): ").split())
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = 'O'
            break
        else:
            print("Invalid move. Try again.")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O' and the AI is 'X'.")
    
    while True:
        print_board(board)
        if check_winner(board) or is_board_full(board):
            break
        human_move(board)
        if check_winner(board) or is_board_full(board):
            break
        ai_move = find_best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'X'
    
    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"The winner is {winner}!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
