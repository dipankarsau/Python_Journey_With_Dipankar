# Q95 Read a sentence from the user. Count and print the total number of
# Vowels (a, e, i, o, u, case-insensitive) present in it, using a for loor. (HW)


text="programing"
ch="aeiouAEIOU"
total=0
for i in text:
    if i in ch:
        total+=1
print(total)




