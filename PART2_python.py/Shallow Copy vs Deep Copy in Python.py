# 1. Shallow Copy

# A shallow copy creates a new outer object, but the nested objects are still shared.

# original = [1, 2, 3, 4]

# copy = original.copy()

# copy.append(100)

# print(original, id(original))
# print(copy, id(copy))



# 2. Deep Copy

# A deep copy creates a new outer object and new nested objects.
import copy

original = [1, 2, 3, 4,[90,100,20],23,445,67]
deep=copy.deepcopy(original)
deep[4][1]=200
print(deep)
print(original)
