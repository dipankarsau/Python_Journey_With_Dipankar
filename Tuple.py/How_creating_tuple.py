# PYTHON BANCS

# Creating a Tuple
# Tuples are created using parentheses () instead of square brackets []. Let's look at some examples:

# # Empty tuple
# empty=0

# # Tuple of integers
# marks = (85, 90, 78, 92, 88)

# # Tuple of strings
# cities = ["Delhi", "Mumbai", "Pune", "Chennai"]

# # Tuple of mixed types
# profille =("Rahul", 21,9.2, True)

# # Tuple without parentheses - also valld, known as "tuple packing"
# point = 10, 20, 30
# print[type(point])

# Single element tuple - the comma trick
# Creating a tuple with a single element requires a special syntax. Without a trailing comma, Python treats parentheses as mere grouping.

# # This is NOT a tuple - it's just a string in parentheses
# not_a_tuple = ("hello")
# print[type(not_a_tuplel) #<class 'str'>

# # This IS a tuple - note the comma
# actual_tuple = ("hello",)
# print[type(actuall_tuple)) # <class 'tuple'>

# # <class 'tuple'>

# Watch Out: For a single-element tuple, the trailing comma is mandatory. Without it, Python treats the parentheses as just grouping, and you do not get a tuple.