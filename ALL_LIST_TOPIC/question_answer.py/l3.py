# Q60. Given two lists, merge them into a
# single new list without modifying the
# originals.

# Hint: Use the + operator or a loop to
# combine. Example: list1 = [1, 2], list2 = [3,
# 4] -> merged = [1, 2, 3, 4]


lst1=[1,2]
lst2=[3,4]
lst3=[]
for i in lst1:
    if i not in lst2:
        lst3.append(i)
for i in lst2:
    if i not in lst1:
        lst3.append(i)
print(lst3)




