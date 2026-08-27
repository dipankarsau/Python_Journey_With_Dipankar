

# Given a list of numbers, use a loop to calculate and print their average.
# You can use len() to get the count of elements, but avoid using
# sum() for the total.





nums =[6,-5,4, 2, 10, 91, -75, 49, 9]
n=len(nums)
total=0
for i in nums:
    total=total+i
    avg=total/n
print(f"avg is ={avg:.2f}")

