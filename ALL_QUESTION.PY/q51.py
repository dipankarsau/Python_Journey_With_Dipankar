# Q59. Reverse a list without using the
# .reverse() method or list slicing
# ([ :: -1]).

# Hint: Think about swapping elements from
# both ends of the list using a loop.
# Example: [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]


a=[1, 2, 3, 4, 5]
n=len(a)
new=[]
for i in range(n-1,-1,-1):
    new.append(a[i])
print(new)
