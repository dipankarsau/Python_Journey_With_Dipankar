
# Question 68
# Create a 3x3 matrix (a nested list) and then use nested loops to calculate and print the sum of all its elements.

# Example:
matrix = [
[1, 2,3],
[4,5,6],
[7,8,9]
 ]

# Expected output for this example: 45
row=len(matrix)
column=len(matrix[0])
total=0
for i in range(0,row):
    for j in range(0,column):
        total=total+matrix[i][j]
print(total)