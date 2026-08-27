# Q40. Write a function called discount_price that takes original_price
# and discount_percent as parameters and prints the final
# price after discount.


def discount_price(original_price,discount_percent):
    discount=original_price*discount_percent/100
    final_result=original_price-discount
    return int(final_result)
a=int(input(" enter your price:-"))
b=int(input(" applied discount:-"))
print(discount_price(a,b))