# Q102 Longest Word
# Take a sentence as input. Print the longest word in it
sentence = "Anirudh is learning Python programming every single day"
a=sentence.split()
longest_count=0
word=0

for i in a:
    if len(i)>longest_count:
        longest_count=len(i)
        word=i
print(word)

