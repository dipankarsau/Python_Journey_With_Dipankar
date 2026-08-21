# PYTHON BASICS

# Sorting Nested Data with Lambda
# When working with complex data structures like lists of dictionaries or dictionaries that need custom sorting, the sorted() function becomes incredibly powerful when combined
# with a 1ambda function. A 1ambda function allows you to define a small, anonymous function directly within the key argument of sorted(), specifying precisely what value to use for
# comparison.

# Sorting a List of Dictionaries

# To sort a list of dictionaries by a specific key, we use a 1ambda function to tell sorted() which dictionary element to use as the sorting key:

# students= [
# {"name": "Rahul", "marks": 85},
# {"name": "Priya", "marks": 92},
# {"name": "Karan", "marks": 78},
# {"name": "Sana", "marks": 95}

# # Sort by marks (ascending)
# by_marks = sorted(students, key=lambda s: s["marks"])
# print("Sorted by marks (ascending):")
# for s in by_marks:
# print(s)
# # Output:
# # {'name': 'Karan', 'marks': 78}
# # {'name': 'Rahul', 'marks': 85}
# # {'name': 'Priya', 'marks': 92}
# # {'name': 'Sana', 'marks': 95}

# # Sort by marks (descending)