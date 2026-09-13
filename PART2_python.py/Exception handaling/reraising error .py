def check_age():

    try:
        age = int(input("Enter your age: "))

        if age < 0:
            raise ValueError("Age cannot be negative")

        elif age >= 150:
            raise ValueError("Age is not real")

    except ValueError as e:
        print(f"Inside function Error = {e}")
        raise
    except Exception as e:
        print(f"inside function error{e} ")
      


try:
    check_age()

except Exception as e:
    print(f"Outside error = {e}")

else:
    print("Success")