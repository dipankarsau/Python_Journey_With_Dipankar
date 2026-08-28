# Given a 4x4 matrix, print only the border elements and replace the inner
# elements with an asterisk (*).
# Input:
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# Expected Output:
# 1 2 3 4
# 5 * * 8
# 9 * * 12
# 13 14 15 16



matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]

row=len(matrix)
colm=len(matrix[0])

for i in range(0,row):
    for j in range(0,colm):
        if i==0 or j==0 or i==row-1  or j==colm-1:
            print(matrix[i][j], end=' ')
        else:
            print("*", end=' ')
    print()