# 1 * 3 *
# * 6 * 8
# 9 * 11 *
# * 14 * 16


matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

row=len(matrix)
col=len(matrix[0])
for i in range(0,row):
    for j in range(0,col ):
        if (i+j)%2==0 :
            print(matrix[i][j], end=' ')
        else:
            print("*", end=' ')
    print()