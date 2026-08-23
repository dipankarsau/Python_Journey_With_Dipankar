# PYTHON BASICS

# What is a Set in Python?
# A set is a collection of values where every value is unique. If you try to add a duplicate, it simply gets ignored. Sets are perfect when you care about what is
# present, but not about order or how many times it appears.

# # List can have duplicates
# emails_list = ["a@gmai.com", "b@gmail.com", "a@gmai.com"]
# print(f"List with duplicates: (emails_list)")
# # Output: ['a@gmail.com', 'b@gmail.com', 'a@gmail.com']

# #Set automatically removes duplicates
# emails_set = {"a@gmail.com", "b@gmail.com", *a@gmail.com"}
# print(f"Set after removing duplicates: (emails_set)")
# # Output: ['a@gmaill.com', 'b@gmail.com'} (order may vary)

# This example clearly demonstrates how sets maintain only unique elements, making them ideal for tasks like filtering out redundant data.

# Key Properties of Sets

# Unordered
# There is no concept of a first or last element;
# the order of elements is not guaranteed and
# can change.

# Unique Values Only
# Sets inherently store only distinct elements,
# automatically discarding any duplicates
# added

# Mutable

# You can add or remove items from a set
# after it has been created.

# No Indexing
# Elements cannot be accessed by their
# position (index) because sets are unordered.

# Immutable Elements
# The elements within a set must be
# immutable (e.g., strings, numbers, tuples).
# Lists or other sets cannot be elements of a
# set

# Sets are highly efficient for operations like checking if a value exists, removing duplicates from a collection, or performing mathematical set operations such
# as unions and intersections. They are a fundamental data structure for tasks where membership testing and uniqueness are paramount.
