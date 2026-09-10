class Money:
    def __init__(self,amount):
        self.amount=amount
    def __eq__(self,other):
        return self.amount==other.amount
    def __lt__(self, other):
        return self.amount < other.amount
    def __le__(self, other):
        return self.amount <= other.amount
    def __gt__(self, other):
        return  self.amount>other.amount
    def __ge__(self, other):
        return self.amount >= other.amount
a=Money(15000)
b=Money(8000)
print(a==b)
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)