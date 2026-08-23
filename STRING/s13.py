# Q105: Palindrome Check
# Write a function is_palindrome(text) that returns True if the given
# string is a palindrome (ignoring case and spaces).

name="racecar"
a=name.lower().replace(" ", "")
if a==a[::-1]:
    print("true")
else:
    print("flase")