#  Take two numbers as input. Without using *
# , calculate and print their product
# using += in a way that adds the first number to itself the
# second number of times. (Think carefully.)


a=int(input("enter a number:-"))
b=int(input("enter a number:-"))

result=0
for i in range(0,a):
    result=result+b
print(result)