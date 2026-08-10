# Q47. Write a function power(base, exp) that returns base raised to exp using a
# loop - no ** operator or pow() allowed.

def power(base, exp):
    result = 1

    for i in range(exp):
        result = result * base

    return result

print(power(2, 4))
