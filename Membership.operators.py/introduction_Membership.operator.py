# Membership Operators

# Membership operators are used to test if a sequence (like a list) contains a specified element. They return a Boolean value (True or False) based on the
# result of the check, making them highly useful for conditional logic.

# in - Check for Membership

# This operator returns True if the specified value is found within the list,
# and False otherwise.
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # Output: True
print("grape" in fruits) # Output: False

# not in - Check for Non-Membership

# This operator returns True if the specified value is NOT found within the
# list, and False otherwise.


fruits = ["apple", "banana", "cherry"]
print("grape" not in fruits) # Output: True
print("banana" not in fruits) # Output: False