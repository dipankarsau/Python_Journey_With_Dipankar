# ASk A NAME,AGE,GEMDER,PRINT
def greet(n, a, g):
    print(f"Hey {n}, your age is {a}, your gender is {g}")


n = input("Enter your name: ")
a = int(input("Enter your age: "))
g = input("Enter your gender: ")

greet(n, a, g)