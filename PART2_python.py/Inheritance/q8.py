#  Write a program with class Bill. The users have the option to pay the bill either by cheque or by cash. Use the inheritance to model this situation.

class Bill:
    def __init__(self, amount):
        self.amount=amount
class Cash(Bill):
    def __init__(self, amount, enteryourcash): 
        

        super().__init__(amount)
        self.enteryourcash=enteryourcash
        if self.enteryourcash>0 and self.enteryourcash<=self.amount:
            self.amount=self.amount-self.enteryourcash
            
        else: 
           print( " invalid amount")
    def show_balance(self):
         return self.amount
class Cheque(Bill):
    def __init__(self,amount, enteryourcheque):
        super().__init__(amount)
        self.enteryourcheque=enteryourcheque
        if self.enteryourcheque>0 and self.enteryourcheque<=self.amount:
            self.amount=self.amount-self.enteryourcheque
           
        else: 
                   print(" invalid amount")
    def show_balance(self):
             return self.amount
        
C=Cash(2000,1000)
CH=Cheque(5000,3000)
print(C.show_balance())
print(CH.show_balance())


        
        
        