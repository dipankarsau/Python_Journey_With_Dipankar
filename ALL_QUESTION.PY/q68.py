# 1  2  3  4  5
# 6  7  *  * 10
# 11 *  13 * 15
# 16 *  * 19 20
# 21 22 23 24 25


matrix = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9, 10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
row=len(matrix)
col=len(matrix[0])
for i in range(0,row):
    for j in range(0,col ):
        if i==0 or j==0 or i==row-1  or j==col-1 or i==j:
            print(matrix[i][j], end=' ')
        else:
            print("*", end=' ')
    print()