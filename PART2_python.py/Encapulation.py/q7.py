# Coding Challenge: Inventory Management System 📦
# Create a class called Inventory to manage product stock in a shop.
# Requirements (English)
# 1. The constructor should accept product_name, stock, and price.
# 2. Store stock and price as private variables.
# 3. Create an add_stock(quantity) method:
#    - If the quantity is positive, increase the stock.
#    - Otherwise, print "Invalid Quantity".
# 4. Create a sell_product(quantity) method:
#    - If the quantity is zero or negative, print "Invalid Quantity".
#    - If the requested quantity exceeds available stock, print "Insufficient Stock".
#    - Otherwise, decrease the stock by the sold quantity.
# 5. Create a show_stock() method to display the current stock.
# 6. Create a show_inventory_value() method to display the total value of the available stock.

class InventoryManagement:
    def __init__(self, product_name, stock, price):
            self.product_name=product_name
            self.__stock=stock
            self.__price=price
    def add_stock(self,quantitiy):
        if quantitiy>0:
            self.__stock=self.__stock+quantitiy
        else: 
            print(" invalid quantity")
    def sell_product(self, quantity):
        if quantity<=0:
            print(" invalid quantity")
        elif quantity > self.__stock:
            print(" invalid quantity")
        else: 
            self.__stock=self.__stock-quantity
            self.__price=self.__price*self.__stock
    def show_stock(self):
        print(self.show_stock)
    def show_inventory_value( self):
        print(self.__price)
I=InventoryManagement("laptop", 10, 50000)
I.add_stock(2)
I.sell_product(3)
I.show_stock()
I.show_inventory_value()

