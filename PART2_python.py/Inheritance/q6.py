# Write a program that has a class Point. Define another class Location which has two objects (Location & Destination) of class Point. Also define a function in Location that prints the reflection of Destination on the x axis.





class POint:
    def __init__(self, location, destination):
        self.location=location
        self.destination=destination
class Location(POint):
   def __init__(self, location, destination):
       super().__init__(location,destination)
   def show(self):
       print(self.location, self.destination*-1)
L=Location(3,-4)
L.show()