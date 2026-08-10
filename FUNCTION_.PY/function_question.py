# Q46. Write a function fizzbuzz(n) that takes a single number and prints
# "Fizz
# "
# if it'
# s divisible by 3,
# "Buzz
# " if it'
# s divisible by 5,
# "FizzBuzz
# " if it'
# s divisible
# by both, otherwise print the number itself.


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

fizzbuzz(12)
fizzbuzz(15)
fizzbuzz(33)
fizzbuzz(7)
