try:

    num1=int(input("enter a number:-"))
    num2=int(input("enter a number:-"))
    print(f'{num1/num2}')
except ZeroDivisionError:
    print(" cannot divide by zero , please enter proper integers")
except ValueError:
    print("please enter proper")
except :
    print("some error occureed")