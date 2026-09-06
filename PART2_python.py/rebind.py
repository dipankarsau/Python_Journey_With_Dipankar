# Re-binding
# Re-binding means assigning a variable to a new object.


def rebind(x):
    x=[1,2,3]
    print(f" the inside is {x}")

num=[10,20,30]
rebind(num)
print(f"outside is {num}")