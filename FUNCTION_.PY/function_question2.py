# Q48. Write a function tax_calculator(income) that takes annual income and returns
# the tax amount based on these slabs:
# Up to 2,50,000 → No tax
# 2,50,001 to 5,00,000 → 5%
# 5,00,001 to 10,00,000 → 20%
# Above 10,00,000 → 30%


def tax_calculator(income):
    tax = 0

    if income <= 250000:
        tax = 0

    elif income <= 500000:
        tax = income * 5 / 100

    elif income <= 1000000:
        tax = income * 20 / 100

    else:
        tax = income * 30 / 100

    return tax


print(tax_calculator(500001))
print(tax_calculator(6000000))


