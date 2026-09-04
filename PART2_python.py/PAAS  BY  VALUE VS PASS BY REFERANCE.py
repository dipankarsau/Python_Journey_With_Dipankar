# paas by value


def greet(x):

    x=x+1
    print(F"inside num is  {x}",id(x))


num =10
greet(num)
print(f" outside nume is {num}",id(num))




# pass by referance
def grret(x):
    x.append(10)
    print(f"inside function is{x}",id(x))
num=[1,2,3]
grret(num)
print(f" outside num is {num}",id(num))