###rotate array(n*n array ratate a clockwise direction
##method 1: switch row and col(O(N^2))
def rotate(matrix):
    n = len(matrix)
    result = [[0]*(n) for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            result[j][n-1-i] = matrix[i][j]
    
    for x in result:
        print(x, sep=' ')
        
##method 2: clockwise square(in-place)
def rotate_in_place(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            ##left -> top
            matrix[first][i] = matrix[last-offset][first]
            ##bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]
            ##right -> bottom
            matrix[last][last-offset] = matrix[i][last]
            ##top -> right
            matrix[i][last] = matrix[first][i]
    for x in matrix:
        print(x,sep=' ')
