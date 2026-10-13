# Mobile Recharge System


class MobileWallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def recharge(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid Amount")

    def use_balance(self, amount):
        if amount <= 0:
            print("Invalid Amount")
        elif amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount

    def transfer_balance(self, other_wallet, amount):
        if amount <= 0:
            print("Invalid Amount")
        elif amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.use_balance(amount)
            other_wallet.recharge(amount)

    def show_balance(self):
        print(self.__balance)


m1 = MobileWallet("Rahul", 1000)
m2 = MobileWallet("Boltu", 500)

m1.recharge(5000)
m1.use_balance(200)
m1.transfer_balance(m2, 100)

m1.show_balance()
m2.show_balance()
