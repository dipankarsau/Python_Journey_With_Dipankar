class Vehicle:
    def __init__(self, brand: str):
        print("this is vehicle constructor")
        self.brand = brand


class Car(Vehicle):
    def __init__(self, fuel: str):
        print("this is car constructor")
        super(). __init__("maruti")
        self.fuel = fuel
    def display(self):
        print(f" you have a {self.brand}car with{self.fuel}")


car = Car("petrol",)
car.display()