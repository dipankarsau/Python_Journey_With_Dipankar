# paas by value


# def greet(x):

#     x=x+1
#     print(F"inside num is  {x}",id(x))


# num =10
# greet(num)
# print(f" outside nume is {num}",id(num))




# pass by referance
# def grret(x):
#     x.append(10)
#     print(f"inside function is{x}",id(x))
# num=[1,2,3]
# grret(num)
# print(f" outside num is {num}",id(num))


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


def greet(person):
    print("Hi my name is", person.name, "I am a", person.gender)

    p1 = Person("ankit", "male")
    return p1


p = Person("nitish", "male")

x = greet(p)

print(x.name)
print(x.gender)