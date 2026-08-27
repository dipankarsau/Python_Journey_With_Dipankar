# Given a list of numbers, write Python code using a loop to find and print the largest element. Do not use the built-in max() function.

numbers = [12, 45, 7, 89, 34, 23, 67]

largest = 0

for i in numbers:
    if largest < i:
        largest = i

print(largest)