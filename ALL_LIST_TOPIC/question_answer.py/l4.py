
# Given a list, remove all duplicate elements while
# preserving the original order of the unique items.

# Example input:
# data = [10, 20, 30, 20, 10, 40, 50,
# 40]
# Expected output: [10, 20,30,40,
# 50]

# data = [10, 20, 30, 20, 10, 40, 50,
# 40]
# new=[]
# for i in data:
#    if i in data and i not in new :
#       new.append(i)
# print(new)


# using function

# def original(data):
#     new = []

#     for i in data:
#         if i not in new:
#             new.append(i)

#     return new


# data = [10, 20, 30, 20, 10, 40, 50, 40]

# print(original(data))