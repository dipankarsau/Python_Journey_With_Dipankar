class Customer:
    def __init__(self, name,gender, address):
            self.name=name
            self.gender=gender
            self.address=address
    def show(self):
          print(self.address.getter())
          print(self.address.pin)
          print(self.address.state)
class Addrees:
    def __init__(self, city, pin, state):
            self.__city=city
            self.pin=pin
            self.state=state
    def getter(self):
          return self.__city


Add=Addrees("kolkata",721430, " west bengal")
cus=Customer("akask", " male", Add)
cus.show()
    