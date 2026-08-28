# Create a list containing the length of each word.

words = ["apple", "cat", "banana", "dog"]
n=len(words)
new=[len(words[i]) for i in range(0,n)]
print(new)