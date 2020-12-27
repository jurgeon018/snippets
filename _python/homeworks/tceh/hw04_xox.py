import random

EQ_X = 'x'
EQ_O = 'o'
EMPTY = ' '
COUNT = 9

def add_board():
    board = []
    for i in range(COUNT):
        board.append(EMPTY)
    return board

def write_board(board):
    print("\n")
    print("\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def pieces():
    pass

def human_step(board):
    pass

def computer_step(board):
    pass

def winner(board):
    WAYS_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    for i in WAYS_WIN:
        if board[i[0]] == board[i[1]] == board[i[2]] != EMPTY:
            return board[i[0]]
    if EMPTY not in board:
        return 'Ничья'

def legal_moves(board):
    pass

def next_turn(turn):
    pass

def main():
    write_board(add_board())
    print(add_board())

if __name__ == '__main__':
    main()
