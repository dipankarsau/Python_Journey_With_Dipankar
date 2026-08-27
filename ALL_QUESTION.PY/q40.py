# Write a function called min_of_three that takes three numbers and returns
# the smallest without using any built-in function.

def min_of_three(a,b,c):
    if a<=b and a<=c:
        return f" the smaller is {a}"
    elif b<=a and b<=c:
        return f" the smaller is {b}"
    else:
        return F" the smaller is {c}"
    
 
a=int(input(" enter a number:-"))
b=int(input(" enter a number:-"))
c=int(input(" enter a number:-"))
print(min_of_three(a,b,c))