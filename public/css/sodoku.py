def solveSudoku(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                for k in range(1, 10):
                    if solver(board, i, j, k):
                        board[i][j] = k
                        if solveSudoku(board):
                            return board
                        board[i][j] = 0
                return False
    return board


def solver(board, x, y, num):
    for i in range(9):
        if board[x][i] == num:
            return False
    for i in range(9):
        if board[i][y] == num:
            return False
    x0, y0 = (x//3)*3, (y//3)*3

    for i in range(3):
        for j in range(3):
            if board[i+x0][j+y0] == num:
                return False
    return True


board = solveSudoku([[0, 0, 0, 8, 0, 0, 0, 0, 9], [0, 1, 9, 0, 0, 5, 8, 3, 0], [0, 4, 3, 0, 1, 0, 0, 0, 7], [4, 0, 0, 1, 5, 0, 0, 0, 3], [
                    0, 0, 2, 7, 0, 4, 0, 1, 0], [0, 8, 0, 0, 9, 0, 6, 0, 0], [0, 7, 0, 0, 0, 6, 3, 0, 0], [0, 3, 0, 0, 7, 0, 0, 8, 0], [9, 0, 4, 5, 0, 0, 0, 0, 1]])
for row in board:
    print(row)
