# Q58. Find the largest and smallest number
# in a list without using built-in functions like
# max() or min().


nums=[4,7,3,8,1,1,2,10,9,6,1,1,1]
a=nums[0]
b=nums[0]

for i in  nums:
    if i>a:
        a=i
    if i <a:
        b=i
print(f" the greatsr number is{a} ")
print(f" the smaller number is b{b} ")

    
        