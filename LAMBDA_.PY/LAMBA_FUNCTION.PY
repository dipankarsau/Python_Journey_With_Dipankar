# Lambda Functions
# A lambda function is a small anonymous function written in a single line. It
# is useful when you need a simple function for a short period and do
# not want to formally define it with def.
# def square(num):
#     return num*num

# print(square(2))
# square=lambda num:num*num
# print(square(2))


# def is_adult(age):
#     if age>=18:
#         return True

# print(is_adult(18))
is_adult = lambda age: True if age >= 18 else False

print(is_adult(18))