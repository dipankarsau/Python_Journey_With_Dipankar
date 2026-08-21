# PYTHON BASICS

# What is a Dictionary in Python?
# A dictionary in Python is an unordered collection of data values used to store data in key-value pairs. Think of it like a real-world dictionary where you look up
# a word (the key) to find its definition (the value), or a phone book where a name (key) leads you to a phone number (value).

# # List - just values, accessed by position
# marks - [85, 90, 78]
# print(marks[0]) #85 - but what does 85 stand for?

# # Dictionary - values labelled with meaningful keys
# marks = {"math": 85, "science": 90, "english": 78}
# print(marks["math"]) #85 -crystal dlear what ths means

# Key Properties of a Dictionary

# Key-Value Pairs
# Every value is stored under a unique,
# descriptive key, making data retrieval
# intuitive.

# Unordered

# Dictionaries dont rely on index position; data
# is accessed via keys. (Note: Python 3.7+
# preserves insertion order.)

# Mutable

# Dictionaries are dynamic; you can add,
# change, or remove key-value pairs after
# creation.

# Unique Keys
# Each key within a dictionary must be unique. Duplicate keys will simply
# overwrite previous entries.

# Immutable Keys
# Keys must be of an immutable data type (e.g., strings, numbers, tuples).
# Lists and other mutable objects cannot be used as keys.