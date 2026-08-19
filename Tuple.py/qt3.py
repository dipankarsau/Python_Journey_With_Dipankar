def tuplee(my_tuple):
    total = sum(my_tuple)
    highest = max(my_tuple)
    lowest = min(my_tuple)
    average = total / len(my_tuple)

    return highest, lowest, total, average


my = (32, 4, 56, 78, 90, 45)

ans1, ans2, ans3, ans4 = tuplee(my)

print(f"The highest is {ans1}")
print(f"The lowest is {ans2}")
print(f"The total is {ans3}")
print(f"The average is {ans4}")