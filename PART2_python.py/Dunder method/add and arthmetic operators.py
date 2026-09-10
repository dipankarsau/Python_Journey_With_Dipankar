class Distance:
    def __init__(self,km):
        self.km=km
    def __add__(self, other):
        return  self.km+other.km
    def __mul__(self, other):
        return self.km*other
    def __sub__(self,other):
        return self.km-other.km
    
    

d2=Distance(30)
d1=Distance(40)
print(d1+d2)
print(d1*3)
print(d2-d1)
