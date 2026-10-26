class Phone:
    def __init__(self, price, brand, camera) :
        print(" inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera


class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        print(" inside smart constructor")
        super().__init__(price,brand,camera)  
        self.os=os
        self.ram=ram
        print(" inside smartphone constructor")

s=SmartPhone(2000, "samsung", 12, "anroid", 2)   
print(s.price  )       