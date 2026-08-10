# Q43. Write a function called absolute_value that takes a number and returns
# its absolute value without using the built-in abs() function
def absolute_value (num):
    if  num>=0:
        return num
    return num*-1

print(absolute_value(-20))
print(absolute_value(-9))
print(absolute_value(+20))


    