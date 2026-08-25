#  Take two numbers as input from the user. Print their sum, difference,
# product, and remainder.
# a=int(input("enter a number:-"))
# b=int(input("enter a number:-"))
# print(a+b,a-b,a%b,a*b)




def greeet(a,b):
    c=a+b,a-b,a%b,a*b
    return c
a=int(input("enter a number:-"))
b=int(input("enter a number:-"))
print(greeet(a,b))