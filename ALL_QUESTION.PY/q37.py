# Q39. Write a function called find_max that takes three numbers as
# parameters and prints the largest one.

def find_max(a, b, c):
    if a > b and a > c:
        return f"the greatest number is {a}"
    elif b > a and b > c:
        return f"the greatest number is {b}"
    else:
        return f"the greatest number is {c}"


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

print(find_max(a, b, c))