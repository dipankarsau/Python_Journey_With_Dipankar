# Q62. Separate a list of integers into two distinct lists: one containing all the
# # even numbers and the other containing all the odd numbers.

def greet(nums):
    even=[]
    odd=[]
    for i in nums:
        if i%2==0:
            even.append(i)
        if i%2!=0:
            odd.append(i)
    return f"the even number is :-{even} , the odd number is {odd}"
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(greet(nums))
