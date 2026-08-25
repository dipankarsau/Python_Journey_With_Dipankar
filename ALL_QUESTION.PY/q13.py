# ake three numbers as input. Print the largest of the three without using any
# # built-in function
num1=int(input("enter your number:-"))
num2=int(input("enter your number:-"))
num3=int(input("enter your number:-"))
if num1>num2 and num1>num3:
    print(f" the highest number is:- {num1}")
elif num2>num1 and num2>num3:
    print(f"the highest number is:-{num2}")
else:
    print(num3)
