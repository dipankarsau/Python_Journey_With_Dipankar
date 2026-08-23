# Take a username as input. Strip any spaces from both sides and check
# if the cleaned name starts with a letter (not a digit). Print "Valid" or
# "Invalid".
name="  dipankar"
a=name.strip()
if a[0].isdigit():
    print("invaild")
else:
    print("valid")