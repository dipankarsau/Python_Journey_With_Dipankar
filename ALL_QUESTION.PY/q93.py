# Given two lists a, b. Check if two lists have at least one element
# common in them.

lst1 = [3, 6, 7, 5, 55, 3, 1, 2, 2, "Python", "Anirudh"]
lst2 = [7, 8, 5, 6, 1, "Anirudh"]
print(set(lst1) & set(lst2))