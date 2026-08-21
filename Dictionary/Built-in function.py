# len(): Count Items
# Returns the total number of key-value pairs (items) in the dictionary, indicating its
# size

# PYTHON BASICS

# Built-in Functions on Dictionaries
# Python provides several convenient built-in functions that can be directly applied to dictionaries or their views (keys, values, items) to perform common operations like counting
# elements, finding totals, or sorting. These functions simplify data manipulation and offer efficient ways to work with dictionary contents.

# #

# min() / max(): Find Extremes
# Identifies the smallest or largest key in a dictionary by default. To find the
# min/max value, apply it to .values().

# pythonmarks = {"math": 85, "science": 92, "english": 78, "hindi": 60}

# # len() - number of key-value pairs
# print(len(pythonmarks))

# # sum() on values
# print(sum(pythonmarks.values()))

# # min() and max() on values
# print(min(pythonmarks.values()))
# print(max(pythonmarks.values()))

# # min() and max() on keys (by default it uses keys, sorted alphabetically)
# print(min(pythonmarks))
# print(max(pythonmarks))

# sum(): Aggregate Values
# Calculates the sum of all numeric values in a dictionary. When used directly on a
# dictionary, it sums its keys (if numeric). For values, explicitly use .values().

# sorted(): Order Elements
# Returns a new sorted list of keys from the dictionary. To get a sorted dictionary by
# keys or values, further processing with . items() and dict() is needed.

# # Output: 4

# # Output: 315

# # Output: 60
# # Output: 92

# # Output: english
# # Output: science