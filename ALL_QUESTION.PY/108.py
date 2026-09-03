# Q107. Reverse Word Order

# Take a sentence as input. Reverse the order of words (not the characters in
# each word). Example: "Python is fun" -> "fun is Python".


example="fun is python language"
example=example.split()
example=example[::-1]
print(" ".join(example))
