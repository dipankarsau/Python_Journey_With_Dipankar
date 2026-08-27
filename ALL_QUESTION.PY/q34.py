# Q36. Write a function that print all the factors of a number entered by user.

def greet(num):
    factor=1
    for i in range(1,num+1):
        factor=factor*i
    return factor
num=int(input("enter a number"))
print(greet(num))