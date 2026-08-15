
# Given a list of numbers (which may contain duplicates), write a
# Python script that takes an integer as input from the user and
# removes all occurrences of that integer from the list.

# # Example input list:
# my_list = [10,20,10, 30, 20, 10, 40]
# # If user enters 10, expected output: [20, 30, 20,
# 40]

num=int(input("enter a number"))
my_list = [10,20,10, 30, 20, 10, 40]
new=[]
for i in my_list:
    if i!=num:
        new.append(i)
print(new)

