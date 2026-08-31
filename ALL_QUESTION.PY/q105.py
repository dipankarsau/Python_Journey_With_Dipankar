# Q103. Username Validation

# Take a username as input. Strip any spaces from both sides and check if the
# cleaned name starts with a letter (not a digit). Print "Valid" or "Invalid".


def valid(username:str):
    username=username.strip()
    if username[0].isdigit():
        return "invalid"
    return "valid"

username="  anirudh123"
print(valid(username))
