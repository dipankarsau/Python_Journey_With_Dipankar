class InsufficientFundsError(Exception):
    pass
def withdraw(balance,withdraw):
    if withdraw>balance:
        raise InsufficientFundsError("not enough balance")
    print(f" remaning balance={balance-withdraw}")
try:
    withdraw(1000,5000)
except InsufficientFundsError as e:
    print(e)
    print(type(e).__name__)
except Exception as e:
    print(e)
    print(type(e))
    
