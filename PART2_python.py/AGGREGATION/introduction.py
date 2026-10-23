
class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def show(self):
        print(self.name)
        print(self.address.getter())
        print(self.address.pin)
        print(self.address.state)

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.edit_address(new_city, new_pin, new_state)


class Addrees:

    def __init__(self, city, pin, state):
        self.__city = city
        self.pin = pin
        self.state = state

    def getter(self):
        return self.__city

    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state


add = Addrees("kolkata", 721430, "west bengal")
cus = Customer("akash", "male", add)

cus.show()

cus.edit_profile("akash", "mumbai", 700126, "maharashtra")

cus.show()
