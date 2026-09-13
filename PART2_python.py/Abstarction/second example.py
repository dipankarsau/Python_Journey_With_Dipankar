
from abc import ABC, abstractmethod
class Bank(ABC):
    @ abstractmethod
    def security(self):
        pass
class Mobileapp(Bank):
    def __init__(self,l):
        self.l=l
    def security(self):
        return self.l *self.l
a=Mobileapp(4)
print(a.security())