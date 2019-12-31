###minesweeper
import random
def minesweeper(m, n, p):
    board = [[None]*(n+2) for i in range(m+2)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            r = random.random()
            board[i][j] = -1 if r < p else 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            print('*', end = ' ') if board[i][j]==-1 else print('.', end = ' ')
        print()
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if board[i][j] != -1:
                for ii in range(i-1, i+2):
                    for jj in range(j-1,j+2):
                        if board[ii][jj] == -1:
                            board[i][j] += 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            print('*', end = ' ') if board[i][j] == -1 else print(board[i][j], end = ' ')
        print()
    
   