# Q58. Find the largest and smallest number
# in a list without using built-in functions like
# max() or min().

# Hint: Use a loop and a variable to track the
# current largest/smallest as you go through
# the list. Example: if the list is [3, 1, 4, 1, 5],
# the largest is 5 and smallest is 1.

a=[3, 1, 4, 1, 5]

largest=a[0]
smallest=a[0]

for i in a:
    if i>largest:
        i=largest
    if i<smallest:
        smallest=i
print(f" the largest is {largest}")
print(f"the smallest is {smallest}")