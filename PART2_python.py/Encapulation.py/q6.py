# Requirements
# 1. Create a class named ShoppingCart.
# 2. The constructor should accept customer_name.
# 3. Store customer_name as an instance variable.
# 4. Store total_price as a private variable and initialize it to 0.
# 5. Create an add_item(price) method:
#    - If the price is positive, add it to the total price.
#    - Otherwise, print "Invalid Price".
# 6. Create a remove_item(price) method:
#    - If the price is positive and does not exceed the total price, subtract it.
#    - Otherwise, print "Invalid Amount".
# 7. Create a show_total() method to display the current total price.



class Shoppingcart:
    def __init__(self, customer_name):
        self.customer_name=customer_name
        self.__total_price=0
    def add_item(self, price):
        if price<0:
            print(" invalid price")
        else: 
            self.__total_price=self.__total_price+price
    def remove_item(self, price):
        if price>0 and price<=self.__total_price:
            self.__total_price=self.__total_price-price
        else: 
            print(" invalid amount")
    def setter(self):
        print(self.__total_price)


s=Shoppingcart("amon")
s.add_item(300)
s.remove_item(200)
s.setter()