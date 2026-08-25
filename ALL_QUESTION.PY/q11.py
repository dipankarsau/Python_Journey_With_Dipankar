# : Take a year as input. Check if it is a leap year. A year is a leap
# year if it is divisible by 4, but not by 100, unless it is also
# divisible by 400.

user = int(input("enter a year"))

if (user % 4 == 0 and user % 100 != 0) or user % 400 == 0:
    print("it is a leap year")
else:
    print("it is not a leap year")