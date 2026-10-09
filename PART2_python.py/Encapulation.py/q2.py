# Requirements

# The class should accept owner and balance as parameters.

# Store balance as a private variable.

# Create an add_money(amount) method to add money to the balance.

# Create a spend_money(amount) method to withdraw money from the balance.

# If the balance is insufficient, print "Insufficient Balance".

# Create a show_balance() method to display the current balance.









class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self):
        while True:
            enter_password = input("Enter your password: ")

            if enter_password == self.__password:
                print("Login successful")
                return
            else:
                print("Wrong password! Try again.")


u1 = User("akash", "12345")
u1.check_password()