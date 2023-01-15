import numpy as np


# board_w = int(input("board width: "))
# board_h = int(input("board height: "))
# board = np.zeros((board_h, board_w))

board = np.zeros((6, 7))


class piont(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


t = 0
lunched = True
while lunched:
    if t == 0:
        print(board)

        col = int(input("p1:"))

        if col == 100:
            lunched = False

        if board[5][col] == 0:
            board[5][col] = 1
        elif board[4][col] == 0:
            board[4][col] = 1
        elif board[3][col] == 0:
            board[3][col] = 1
        elif board[2][col] == 0:
            board[2][col] = 1
        elif board[1][col] == 0:
            board[1][col] = 1
        elif board[0][col] == 0:
            board[0][col] = 1

        t = 1

    if t == 1:
        print(board)
        
        col = int(input("p2:"))

        if col == 100:
            lunched = False

        board[5][col] = 2

        print(board)

        t = 0

