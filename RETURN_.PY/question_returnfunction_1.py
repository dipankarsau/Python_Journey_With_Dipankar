# number is prime or not
def greet(num):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        return True

    return False


print(greet(17))
print(greet(10))
print(greet(7))
print(greet(20))



    