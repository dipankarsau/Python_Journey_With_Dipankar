class Animal:
    def __init__(self,name):
        self.name=name
    def breathe(self):
        print(f"{self.name} is breathing")

class dog(Animal):
    def bark(self):
        print("woof")
class cat(Animal):
    def meow(self):
        print("meow")
class cow(Animal):
    def moo(self):
        print("moo")
d=dog("rex")
d.bark()
d.breathe()