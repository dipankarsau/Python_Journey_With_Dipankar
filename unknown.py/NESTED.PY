age = int(input("Enter your age: "))
certificate = input("Do you have a certificate? (yes/no): ")

if age >= 18:
    if certificate == "yes":
        print("You will be hired")
    else:
        print("Cannot hire due to no certificate")
else:
    print("Cannot hire, age is lower than 18")