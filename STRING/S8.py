# Q100: Sorted Names
# Take a list of names as input (comma separated). Split them, sort them
# alphabetically, and join them back with " | " as separator.
name=input("enter your sentence:-")
a=name.split()
c=sorted(a)


b="| ".join(c)
print(b)