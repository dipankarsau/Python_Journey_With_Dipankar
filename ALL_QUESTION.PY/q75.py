# Write a function get_stats(nums) that takes a tuple of numbers and returns a tuple containing the sum, average, and minimum. Unpack the returned tuple and print each value.

numbers = (10, 20, 30, 40, 50)

def get_stats(nums):
    total=0
    n=len(nums)
    for i in nums:
        total=total+i
    ave=total/n
    a=sum(nums)
    b=min(nums)
    c=ave
    return a,b,c
a,b,c=get_stats(numbers)
print(f" max={a},")
print(f"min={b}")
print(f"average={c}")
