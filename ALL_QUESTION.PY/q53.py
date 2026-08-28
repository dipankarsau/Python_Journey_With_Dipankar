# Q61. Given a list, remove all duplicate elements while preserving the original
# order of the unique items.


def greet(num):
    new=[]
    for  i in num:
        if i not in new:
            new.append(i)
    return new

nums = [1, 5, 4, 5, 5, 6, 5, 4, 3, 5, 6, 7, 6, 7, 1, 1, 1]
print(greet(nums))