# . Take a name as input from the user. Print its first character, its last
# character, and the total length of the name.
name=input("enter your name:-")
total=0
for i in name:
    if i in "aeiouAEIOU":
        total=total+1
print(total)