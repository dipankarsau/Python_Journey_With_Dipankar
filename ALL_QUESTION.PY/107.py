# Q105. Palindrome Check

# Write a function is_palindrome(text) that returns True if the given string is
# a palindrome (ignoring case and spaces).

def is_palindrome(text:str):
    text.lower().replace(" ","")
    return text==text[::-1]
text="racecar"
print(is_palindrome(text))