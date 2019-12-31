###given a m*n matrix, if one element is 0, elements in its row and coloumn will be 0
def matrix_trans(matrix):
    m = [None] * len(matrix)
    n = [None] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                m[i] = 1
                n[j] = 1
    
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            if m[i] == 1 or n[j] == 1:
                matrix[i][j] = 0
    for x in matrix:
        print(x, sep=' ')
        