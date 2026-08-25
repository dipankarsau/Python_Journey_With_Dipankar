# A student scored marks in 3 subjects. Take all three as input,
# calculate the total and average, and print both using an f-string


a = int(input("Enter your mark: "))
b = int(input("Enter your mark: "))
c = int(input("Enter your mark: "))

total = a + b + c
ave = total / 3

print(f"total = {total}, average = {ave}")