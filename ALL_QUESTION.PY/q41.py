# 43. Write a function called absolute_value that takes a number and returns
# its absolute value without using the built-in abs() function.


def absolute_value(num):
    if num<0:
        a=num*-1
        return a
    return num

num=int(input(" enter a number:-"))
print(absolute_value(num))