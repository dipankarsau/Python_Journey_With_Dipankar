# Take a sentence as input. Capitalize only the first letter of each word
# that is longer than 3 characters. Keep the rest as is.

name = input("Enter your word:-")

word = name.split()

result = []

for i in word:
    if len(i) > 3:
        result.append(i.capitalize())
    else:
        result.append(i)

print(" ".join(result))
