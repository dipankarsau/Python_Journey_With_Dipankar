try:
    num1 = int(input("Enter a number1: "))
    num2 = int(input("Enter a number2: "))

    print(f"{num1 / num2}")

except Exception as e:
    print(type(e).__name__)
    print(e)