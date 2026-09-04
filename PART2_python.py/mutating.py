def mutating(x):
    x[0]=100
    print(f" the inside is {x}")

num=[10,20,30]
mutating(num)
print(f"outside is {num}")