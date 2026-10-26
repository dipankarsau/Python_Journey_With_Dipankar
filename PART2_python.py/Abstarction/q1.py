# Payment System
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class Creditcard(Payment):
    def pay(self,amount):
        if amount>0 :
            print(" paymenyt succesfully")
        else:
            print(" invalid amount")
C=Creditcard()
C.pay(500)
C.pay(-500)

        