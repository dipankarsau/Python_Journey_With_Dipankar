# Q102. Longest Word

# Take a sentence as input. Print the longest word in it.

sentence = "Anirudh is learning Python programming every single day"

longest_word = ""
longest_count = 0

word = sentence.split()

for i in word:
    if len(i) > longest_count:
        longest_count = len(i)
        longest_word = i

print(longest_word)

# short way
word = sentence.split()

print(max(word, key=lambda x: len(x)))