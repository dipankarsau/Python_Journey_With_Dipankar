# Q59. Reverse a list without using the
# .reverse() method or list slicing
# ([ ::- 1]).

# Hint: Think about swapping elements from
# both ends of the list using a loop.
# Example: [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]

nums = [1, 2, 3, 4, 5]
a = []
n = len(nums)

for i in range(n-1, -1, -1):
    a.append(nums[i])

print(a)