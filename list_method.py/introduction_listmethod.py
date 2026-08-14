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



# Sorting and Reversing Elements
# .sort() - Sort In-Place
# Sorts the elements of the list in ascending order directly, modifying the original list.

nums = [40, 10, 30, 20, 50]
# sorts in place, modifies original
print(nums) # Output: [10, 20, 30, 40, 50]

nums.sort()





# .reverse() - Reverse In-Place
# Reverses the order of elements in the list directly, modifying the original list.

nums = [10, 20, 30, 40, 50] # Reset for example clarity
# reverses in place
print(nums) # Output: [50, 40, 30, 20, 10]

nums.reverse()





# Searching and counting Elements

# index() - Find Element Index
# Returns the index of the first occurrence of a specified value in the list.

fruits = ["apple", "mango", "banana", "mango"]
print(fruits.index("mango")) # Output: 1 - index of first occurrence





# .sort(reverse=True) - Sort Descending
# Sorts the list in descending order by setting the reverse parameter to True.

nums = [10, 20, 30, 40, 50] # Reset for example clarity
nums.sort(reverse=True) # sorts in descending order
print(nums) # Output: [50, 40, 30, 20, 10]




# .count() - Count Element Occurrences
# Returns the number of times a specified value appears in the list.

fruits = ["apple", "mango", "banana", "mango"]
print(fruits.count("mango")) # Output: 2 - how many times it appears