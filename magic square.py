###magic square: make a square consist of numbers, which sum of numbers in columns, rows and diagonal are the same
def magic_square(n):
    magic = [[0]*(n) for i in range(n)]
    ##post 1 in a certain position
    row = n-1
    col = n//2
    magic[row][col] = 1
    
    ##post other numbers
    for i in range(2, n*n+1):
        ###test whether beyond board
        try_row = (row + 1) % n
        try_col = (col + 1) % n
        
        if (magic[try_row][try_col] == 0):
            row = try_row
            col = try_col
        else:
            row = (row -1 +n) % n
            
        magic[row][col] = i
        
    for x in magic:
        print(x, sep='')
            
        