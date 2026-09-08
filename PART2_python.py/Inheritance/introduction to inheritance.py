class Vehicle:
    def __init__(self,brand):
        self.brad=brand
    def start(self):
        print(f"{self.brad} starting up")


class car(Vehicle):
    def drive(self):
        print(f"{self.brad}is driving")
c=car("toyato")
c.start()
c.drive()