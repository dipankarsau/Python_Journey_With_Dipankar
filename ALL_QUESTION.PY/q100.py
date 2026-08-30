# Q97: Email Validation
# Take an email as input. Validate that it contains exactly one @ and at least
# one .. Print "Valid" or "Invalid".




user=input("enter a  email:-")

if user.count("@")==1 and user.count(".")==1:
      print(user)
else:
    print("enter a valid email")

