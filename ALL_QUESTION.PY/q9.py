# Take two numbers as input. Print the greater of the two. If they are
# equal, print "Both are equal."


num1=int(input("enter a  first number:-"))
num2=int(input("enter a second number:-"))

if num1>num2:
    print(f" the greater number is {num1}")
elif num2>num1:
    print(f" The greater number is {num2}")
else:
    print("bothe are equal")