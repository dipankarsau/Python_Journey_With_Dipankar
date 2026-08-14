# PYTHON BASICS

# List Methods
# List methods are built-in functions that operate directly on a list, allowing you to modify it in place. Unlike built-in functions like sorted() which retum a new list, methods change the original list.

# Adding Elements

# .append() - Add to End
# Adds a single element to the end of the list.

fruits = ["apple", "mango"]
fruits.append("banana")
print(fruits) # Output: ["apple", "mango", "banana"]

# .insert() - Add at Index
# Inserts an element at a specified index. The first argument is the index, the second is the value.

fruits = ["apple", "mango", "banana"]
fruits.insert(1, "kiwi")
print(fruits) # Output: ["apple", "kiwi", "mango", "banana"]


# Removing Elements

# .remove() - Remove by Value
# Removes the first occurrence of a specified value from the list. If the item is not found, it raises a
# ValueError.

fruits = ["apple", "kiwi", "mango", "banana"]
# by value
fruits.remove("mango")
print(fruits) # Output: ["apple", "kiwi", "banana"]


# .pop() - Remove by Index (or Last)
# Removes and returns the element at a given index. If no index is specified, it removes and returns the last
# element.

fruits = ["apple", "kiwi", "banana"]
popped_last = fruits.pop()
# by index
print(f"Popped: {popped_last}, List: {fruits}") # Output: Popped: banana, List: ["apple", "kiwi"]

popped_first = fruits.pop(0)
print(f"Popped: {popped_first}, List: {fruits}") # Output: Popped: apple, List: ["kiwi”]