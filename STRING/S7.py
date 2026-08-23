# Q99: Vowel-Starting Words
# Take a sentence as input. Split it into words and print how many words
# start with a vowel.

# name = input("enter a word:-")

# b = name.split(" ")

# total=0
# for i in b:
#     if i.startswith(("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")):
#         total=total+1
# print(total)


# another way
def greet(name:str):
    vowels="aeiouAEIOU"
    count=0
    a=name.split()
    for i in a:
        if i[0] in vowels:
            count+=1
    return count
name=input("enter you sentence:-")
print(greet(name))
