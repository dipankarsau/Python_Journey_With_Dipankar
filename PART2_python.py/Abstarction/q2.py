# Payment System with Multiple Child Classes


from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCard(Payment):
    def pay(self, amount):
        if amount >0:
            print(" piad using credit card")
        else:
            print(" invalid amopunt")
class Upi(Payment):
    def pay(self, amount):
            if amount >0:
                print(" piad using upi")
            else:
                print(" invalid amopunt")
C=CreditCard()
U=Upi()
C.pay(200)
C.pay(-300)
U.pay(300)
U.pay(-400)