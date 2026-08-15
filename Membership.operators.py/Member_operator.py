nums=[4,7,3,8,1,1,2,10,9,6,1,1,1]
# print(100 in nums)
# target=int(input("enter a number"))
# if target in nums:
#    nums.remove(target)
#    print(nums)
# else:
#    print("target does not exit")

def greet(target):
   if target in nums:
      nums.remove(target)
      return nums
nums=[4,7,3,8,1,1,2,10,9,6,1,1,1]
target=int(input("enter a number"))
print(greet(target))