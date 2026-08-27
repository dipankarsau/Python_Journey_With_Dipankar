# Write a program that takes a list and a target number. Use a loop to determine if the target number exists in the list. Do not use the in operator.

numbers = [10, 25, 7, 42, 18, 33, 50]
target=int(input(" enter your number:-"))
def greet(numbers,target):
    for i in numbers:
        if i==target:
            return "exit in list"
    return " does not exit"

print(greet(numbers,target))