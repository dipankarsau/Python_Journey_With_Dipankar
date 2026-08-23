# Q97: Email Validation
# Take an email as input. Validate that it contains exactly one @ and at
# least one .. Print "Valid" or "Invalid"

# name=input("enter your email:-")
# if name.count("@")==1 and "." in name:
#         print( f" your email is {name}")
# else:
#     print("pleaase enter a valid email")


# using function
def greet(name ):
      if name.count("@")==1 and "." in name:
            return name
      return "please entaer a valid email"
name=input("enter a  email :-")
print(greet(name))