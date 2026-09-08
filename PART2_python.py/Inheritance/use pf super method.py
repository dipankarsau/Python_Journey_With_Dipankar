class Animal:

    def speak(self):
        print("some generic animal")

    def display(self):
        print("this is a display function")


class Dog(Animal):

    def speak(self):
        super().speak()
        self.display()
        print("woof!")


d = Dog()

d.speak()