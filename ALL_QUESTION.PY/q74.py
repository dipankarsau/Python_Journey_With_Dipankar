# Take 5 numbers as input from the user, store them in a tuple, and print the tuple along with its minimum and maximum.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))
num5 = int(input("Enter a number: "))

a = (num1, num2, num3, num4, num5)
print(max(a), min(a))