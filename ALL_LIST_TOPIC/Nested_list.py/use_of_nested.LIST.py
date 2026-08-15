# 3*3
matrix=[[4,8,1],[9,7,2],[5,6,0]]

# for i in range(0,3):
#     for j in range(0,3):
#         print(martix[i][j],end=' ')
#     print()

    # total korta chaila
total=0
for i in range(0,3):
    for j in range(0,3):
        total= total+matrix[i][j]
print(total)
