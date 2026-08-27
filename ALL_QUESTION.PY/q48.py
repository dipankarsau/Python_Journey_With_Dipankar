# Given two lists of the same length, write Python code using a loop to create
# a new list where each element is the sum of the corresponding elements from
# both original lists.





nums1 = [6, 5, 4, 2, 10, 91, -75, 49, 9]

nums2 = [4, 1, 54, 76, 41, 85, 3, 44, 2]

result = []
n=len(nums1)

for i in range(0,n):
    c=nums1[i]+nums2[i]
    
    result.append(c)

print(result)