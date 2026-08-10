# Q42. Write a function called min_of_three that takes three numbers and returns
# the smallest without using any built-in function.

def findd(num1,num2,num3):
    if num1<=num2 and num1<=num3:
        return num1
    elif num2<=num1 and num2<=num1:
        return num2
    else:
        return num3
print(findd(1,2,3))
    


