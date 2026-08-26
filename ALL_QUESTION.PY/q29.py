# Q29. Print the following pattern using nested loops:

#         1
#       1 2 3
#     1 2 3 4 5
#   1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8 9
#   1 2 3 4 5 6 7
#     1 2 3 4 5
#       1 2 3
#         1


for i in range(1,6):
    for k in range(i,5):
        print(" ", end=' ')
    for j in range(1,i*2):
        print(j, end=' ')
    print()

for i in range(1,5):
    for k in range(1,i+1):
        print(" ", end=' ')
    for j in range(1,10-2*i):
        print(j, end=' ')
    print()