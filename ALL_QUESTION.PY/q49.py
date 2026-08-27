#  Write a program that takes a list of numbers and, using a loop, determines
# whether it is sorted in ascending order. Print True if it is sorted,
# and False otherwise.

nums = [3, 6, 8, 9, 13, 17, 18, 23, 45, 58, 79, 100]
n=len(nums)
def greet(nums):
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False
    return True
print(greet(nums))
    
        
        
              
        
        

