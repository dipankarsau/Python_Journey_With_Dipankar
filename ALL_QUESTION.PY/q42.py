# Q47. Write a function power(base, exp) that returns base raised to exp using a
# loop - no ** operator or pow() allowed.


def greet(base,exp):
    num=1
    for i in range(1,exp+1):
        num=num*base
    return num
n=int(input("enter your base:-"))
e=int(input("enyter your exp:-"))
print(greet(n,e))
