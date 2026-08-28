# Create a list containing the square of only even numbers.

nums = [1, 2, 3, 4, 5, 6]
new=[i**2 for i in nums if i%2==0]
print(new)