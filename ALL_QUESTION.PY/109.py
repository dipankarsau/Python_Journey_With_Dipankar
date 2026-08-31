# Take a string as input. Check if it is a valid Indian PAN card number.
# Format: 5 uppercase letters + 4 digits + 1 uppercase letter (Total 10
# characters). Example: ABCDE1234F

user = input("Enter your PAN: ")

n = len(user)

a = user[0:5]
b = user[5:9]
c = user[9]

if n == 10 and a.isupper() and b.isdigit() and c.isupper() and c.isalpha():
    print("Valid")
else:
    print("Invalid")

