# Q65. Write a Python script that iterates through a list of integers and replaces every
# negative number found in the list with the value 0.


def greet(nums):
    n=len(nums)
    for i in range(0,n):
        if nums[i]<0:
            nums[i]=0
    return nums

nums=[1,2,3,4-2,3,-8,9,-4,-3]
print(greet(nums))


