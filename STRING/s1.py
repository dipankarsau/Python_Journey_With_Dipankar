# Q93. Take a name as input from the user. Print its first character, its last
# character, and the total length of the name.
# name="programing"
# n=len(name)
# print(name[0],name[-1],n)


# using function
def greet(name):
    n=len(name)
    return name[0], name[-1],n
print(greet("programing"))