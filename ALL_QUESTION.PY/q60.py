# Q4. Convert every negative number into 0
nums = [1, -2, 3, -4, 5, -6]

new = [0 if nums[i] < 0 else nums[i] for i in range(len(nums))]

print(new)