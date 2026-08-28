# 2 Q63. Create a list containing the squares of numbers from
# 3 1 to 10 (i.e., [1, 4, 9, ... , 100]).


def greet(nums):
    new=[]
    for i in nums:
        c=i*i
        new.append(c)
    return new
nums=[1,2,3,4,5,6]
print(greet(nums))
