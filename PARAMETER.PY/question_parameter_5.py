
# Write a function called discount_price that takes original_price
# and discount_percent as parameters and prints the final
# price after discount.
def discount_price(original_price, discount_percen):
    discount_amount = (discount_percen / 100) * original_price
    final_amount = original_price - discount_amount
    print(f"Your final amount is {final_amount}")


discount_price(100, 50)

discount_price(100, 30)