
# Write a Python script that iterates through a list of integers and
# replaces every negative number found in the list with the value 0.

# # Example input list:
# numbers = [5,-3, 8, -1, 0, -10, 12]
# # Expected output: [5,0,8, 0, 0, 0, 12]
numbers = [5, -3, 8, -1, 0, -10, 12]

new = []

for i in numbers:
    if i < 0:
        new.append(0)
    else:
        new.append(i)

print(new)