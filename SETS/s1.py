# checking if a user has access
allowed_user={"rahul","priya","karan"}
user=input("enter username: -")
if user in allowed_user :
    print("accessses granted")
else:
    print("accesses denied")