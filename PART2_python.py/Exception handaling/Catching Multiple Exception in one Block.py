try:

    num=int(input(" enter a number:-"))
    result=100/num
    print(result)
except(ValueError,ZeroDivisionError):
    print("invalid input.Try again")
    