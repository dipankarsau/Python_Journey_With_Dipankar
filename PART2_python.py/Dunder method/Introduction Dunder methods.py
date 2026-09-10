class Point:
    def __init__(self,x:int,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"point {self.x},{self.y}"
    def __repr__(self):
        return f"point{self.x}, {self.y}"
p=Point(3,4)
p2=Point(6,7)
print(p)
print(p2)
print(repr(p),repr(p2))