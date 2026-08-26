# Q21. Print the following pattern using nested loops:

# *
# * *
# * * *
# * * * *
# * * * * *


for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=" ")
    print()
    