# Write a Python program to check if two given sets have no elements
# in common.

set1 = {5, 6, 2, 1, "Anirudh", 7}
set2 = {"Python", 76, 22, 91, -991,}

c=set1&set2
print(c)
if c==0:
    print("both sets have nothing in common")
else:
    print(f"some common is {c}")