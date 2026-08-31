# Take a sentence as input. Print each word's length next to it. Example:
# Python (6) is (2) great (5)

user=input("enter your word:-")

user=user.split()
for i in user:
    print(i,len(i))