# PYTHON BASICS
# What is a Tuple in Python?
# A tuple is a collection of values stored in a single variable, very similar to a list. The key difference is that a tuple is immutable. Once created, you cannot change,
# add, or remove its elements.

# List - Can be Changed

# cities_list = ["Delhi", "Mumbai", "Pune"]
# cities_list[0] = "Chennai" # Allowed
# print(cities_list) # Output: [ʼChennaiʼ, 'Mumbaiʼ, 'Puneʼ]

# Tuple - Cannot be Changed

# cities_tuple = ("Delhi", "Mumbai", "Pune")
# cities_tuple[0] = "Chennai" # TypeError!
# print(cities_tuple) # Output: TypeError!

# Key properties of a tuple:

#  Ordered - items stay in the order you put them.

#  Allows duplicates - the same value can appear more than once.

# Tuples are used when you want to store data that should not change, such as coordinates, RGB colour values, or database records where the structure or
# content should remain constant.

# Immutable - cannot be modified after creation.

#  Can hold any data type - integers, strings, booleans, even lists.



my_tuple=(1,2,3,"anirudh")
print(my_tuple)

# immutable dont cahnge after creating tuple 
print(my_tuple.count(1))
print(my_tuple.index("anirudh"))
