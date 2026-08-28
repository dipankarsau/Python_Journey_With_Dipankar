# Given a 3x3 matrix, print its upper triangle. Replace all elements in
# the lower triangle (below the main diagonal) with an asterisk (*).
# Input:
# 1 2 3
# 4 5 6
# 7 8 9
# Expected Output:
# 1 2 3
# * 5 6
# * * 9


matrix=[[1,2,3]
        ,[4,5,6],
        [7,8,9]]
rows=len(matrix)
colm=len(matrix[0])

for i in range(0,rows):
    for j in range(0,colm):
        if i<=j:
            print(matrix[i][j], end=' ')
        else:
            print("*", end=' ')
    print()
