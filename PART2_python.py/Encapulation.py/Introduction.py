class Bank:
    def __init__(self,name:str,balance:int):
        self.name=name
        self.__balance=balance

    def deposite(self,amount:int):
        if amount<0:
            print("invaid amount")
        else:
            self.__balance+=amount
    def get(self):
        return self.__balance
s1=Bank("akash",100)
s1.deposite(100)
print(s1.get())