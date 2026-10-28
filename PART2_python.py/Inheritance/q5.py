# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

# Use the following code for your parent Vehicle class.




class Vehicle:
    def __init__(self, seating_capacity):
        self.capacity = seating_capacity


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return capacity


B = Bus(3)
print(B.seating_capacity())
print(B.seating_capacity(30))