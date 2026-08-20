# Q81: Product Price Lookup (HW)
# Construct a dictionary containing four product names and their
# prices. Prompt the user to enter a product name. Use the in
# keyword to check if it exists; if so, display its price. Otherwise,
# inform the user "Product not found."



products = {
    "laptop": 50000,
    "phone": 25000,
    "headphone": 3000,
    "keyboard": 1500
}

user = input("enter your product: ")

if user in products:
    print(products[user])
else:
    print("Product not found")