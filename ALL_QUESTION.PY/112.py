# Write a function most_common_word(text) that returns the word that
# appears most frequently in a given paragraph. Ignore case. If multiple
# words have the same count, return any one.

def most_common_word(text):
    words = text.lower().split()

    most_word = ""
    max_count = 0
    for i in words:
       count = words.count(i)

       if count>max_count:
           max_count=count
           most_word=i
    return most_word


user = "Python is fun and python is easyyyyuuui"

print(most_common_word(user))
           
        

        
