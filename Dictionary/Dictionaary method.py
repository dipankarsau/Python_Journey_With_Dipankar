# PYTHON BASICS

# Dictionary Methods (Part 1)
# Python dictionaries offer several built-in methods to efficiently interact with their contents. The keys0, values(), and iters() methods are particularly useful for
# accessing different components of the dictionary.

# keys[
# Returs a view object that displays a list of all
# the keys in the dictionary. This view object is
# dynamic, meaning it reflects any changes
# made to the dictionary.

# values()
# Retums a view object that displays a list of all
# the values in the dictionary. Like keys(), this
# view updates dynamically when the
# dictionary changes.

# items()
# Retums a view object that displays a list of a
# dictionary's key-value pairs as tuples. This
# combined view also updates dynamically
# with dictionary modifications.

# student = ("name": "Rahul", "age": 21, "city": "Delhi")

# # keys() - returs a view of all keys
# print(student.keys()
# # Output: dict_keys(['name', 'age', 'city'l)

# # values() - returns a view of all values
# print(student.values())
# # Output: dict_values(['Rahull, 21, 'Delhi])

# # items0 - returns a view of all key value pairs as tuples
# print(student.items(00
# # Output: dict_items|[('name', 'Rahull'], ('age', 21), ('city', 'Delhi')])

# # You can convert these views to a list if you need indexing or other list operations
# keys_list = list(student.keys())
# print(keys_list[0]) # Output: name