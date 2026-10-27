
# Bank Account Management System

class BankAccount:
    count = 0

    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.__initial_balance = initial_balance
        BankAccount.count += 1

    def deposit(self, amount):
        if amount > 0:
            self.__initial_balance += amount
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.__initial_balance:
            print("Insufficient balance")
        else:
            self.__initial_balance -= amount

    def get_balance(self):
        return self.__initial_balance

    def add_to_balance(self, amount):
        if amount > 0:
            self.__initial_balance += amount

    def show_details(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.get_balance())


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance, interest_rate):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.add_to_balance(interest)

    def show_details(self):
        super().show_details()
        print("Interest Rate:", self.interest_rate)


# Create objects
a1 = BankAccount("Rahul", 5000)
a2 = SavingsAccount("Amit", 10000, 5)

# Perform transactions
a1.deposit(2000)
a1.withdraw(1000)

a2.deposit(2000)
a2.add_interest()

# Display details
a1.show_details()
print()

a2.show_details()
print()

print("Total Accounts:", BankAccount.count)
