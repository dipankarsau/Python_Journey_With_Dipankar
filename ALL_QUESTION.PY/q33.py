# Q35. Write a function that ask a number from user and prints if that
# number is odd or even.

def greet(num):
    if num%2==0:
        return "even"
    return "odd"
num=int(input("enter your number"))
print(greet(num))