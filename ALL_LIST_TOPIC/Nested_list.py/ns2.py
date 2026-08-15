


# Given a 3x3 matrix as input, print its lower triangle. Replace all elements in the upper triangle (above the main diagonal) with an asterisk (*).

# Input:
#123
#456
#789

# Expected Output:
#1 **
#45*
#789


matrix=[[1,2,3],[4,5,6],[7,8,9],]
r=len(matrix)
c=len(matrix[0])
for i in range(0,r):
    for j in range(0,c):
        if i>=j:
            print(matrix[i][j],end=' ')
        else:
            print("*", end=' ')
    print()