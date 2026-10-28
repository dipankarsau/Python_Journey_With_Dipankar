class Vehicle:
    def __init__(self, setaing_capacity):
        self.seating_capacity=setaing_capacity
    def fare(self):
        return self.seating_capacity*100
class Bus(Vehicle):
    def fare(self):
       total_fare=super().fare()
       maintainace=total_fare*10/100
       return total_fare+ maintainace
B=Bus(50)
print(B.fare())