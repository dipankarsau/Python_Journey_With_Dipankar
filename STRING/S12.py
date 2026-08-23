# Q104: Unique Words Count
# Take a paragraph as input. Print the count of unique words in it (case
# insensitive).
paragraph = "Python is great and Python is fun and learning Python is the best"
words=paragraph.split()
print(len(set(words)))

