# Digital Wallet System 💰

class Digital_wallet:
    def __init__(self, owner, intial_balance):
        self.owner=owner
        self.__initial__balance= intial_balance
    def  get_balance(self) :
        return self.__initial__balance
    def deposit(self, amount):
        if amount >0:
            self.__initial__balance=self.__initial__balance+amount
        else:
            print(" invalid amount")
    def withdraw(self, amount):
        if amount<=0:
            print(" invalid amount")
        elif amount>self.__initial__balance:
            print(" insufficient  balance")
        else:
            self.__initial__balance=self.__initial__balance-amount
    def transfer(self, other_wallet, amount):
        if amount <= 0:
            print("Invalid Amount")

        elif amount > self.__initial__balance:
            print("Insufficient Balance")

        else:
            self.withdraw(amount)
            other_wallet.deposit(amount)

D=Digital_wallet("boltu", 30000)
D1=Digital_wallet("amit", 2000)

D.deposit(1000)
print(D.get_balance())
D.withdraw(25000)
print(D.get_balance())
D.transfer(D1,5000)
print(D.get_balance())
print(D1.get_balance())

