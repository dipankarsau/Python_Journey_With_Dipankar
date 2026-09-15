# import math
# print(math.sqrt(16))
# print(math.floor(5.8))
# print(math.ceil(1.003))


# another way
# import math as m
# pi=3.14
# print(m.sqrt(16))
# print(m.floor(5.8))
# print(m.ceil(1.003))
# print(m.pi)

# another way

# from math  import sqrt, ceil
# print(sqrt(10))
# print(ceil(100))



# / use of random keyword



import random
print(random.random())
print(random.randint(1,78))
print(random.choice(["a","b","c","d","e","f","g","h"]))
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
random.shuffle(letters)

print(letters)
