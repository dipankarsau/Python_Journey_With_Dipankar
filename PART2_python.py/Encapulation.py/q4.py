# Coding Question: ATM Machine System

# Create a class called ATM that simulates a simple ATM machine.

# Requirements

# The class should accept name, pin, and balance as parameters.

# Store pin and balance as private variables.

# Create a check_pin(entered_pin) method that returns True if the PIN is correct; otherwise, it returns False.

# Create a deposit(amount, entered_pin) method to deposit money only when the PIN is correct and the amount is positive.

# Create a withdraw(amount, entered_pin) method that:

# Checks whether the PIN is correct.

# Checks whether the amount is positive.

# Checks whether sufficient balance is available.

# Deducts the money only if all conditions are satisfied.

# Create a show_balance(entered_pin) method that displays the balance only when the PIN is correct.

class ATM:
    def __init__(self, name, pin, balance):
        self.name=name
        self.__pin=pin
        self.__balance=balance
    def chech_pin(self, entered_pin):
        if self.__pin==entered_pin:
            return True
        return False
    
        
           
           
    def deposit(self, amount, enter_pin):
        if self.chech_pin(enter_pin) and amount>0:
            self.__balance=self.__balance+amount
            print(self.__balance)
        elif not self.chech_pin(enter_pin):
            print("wrong pin")
        else:
            print("invalid amount")
    def withdrawl(self, amount, entered_pin):
        if not self.chech_pin(entered_pin):
            print(" invalid pin")
        elif amount<=0:
            print("invalid amount")
        elif amount>self.__balance:
            print(" insuffient balance")
        else:
            self.__balance-=amount
            print(self.__balance)
    def show_balance(self,pin):
        if self.chech_pin(pin):
            print(self.__balance)
        else:
            print(" WRONG PIN")
atm=ATM("akash", "1234", 5000)
atm.deposit(-1000,"1234")
atm.withdrawl(6000,"1234")
atm.show_balance("1234")



       
