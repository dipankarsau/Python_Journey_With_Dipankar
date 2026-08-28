# Given a 3x3 matrix, print only the main diagonal elements and
# replace everything else with an asterisk (*).
# Input:
# 1 2 3
# 4 5 6
# 7 8 9
# Expected Output:
# 1 * *
# * 5 *
# * * 9


matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
row=len(matrix)
colm=len(matrix[0])

for i in range(0,row):
    for j in range(0,colm):
        if i==j:
            print(matrix[i][j], end=' ')
        else:
            print("*", end =' ')
    print()
