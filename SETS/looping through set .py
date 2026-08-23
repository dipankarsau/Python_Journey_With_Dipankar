# Looping Through a Set
# Although sets are unordered collectiona, you can easily iterane over their elementa uaing a for loop. This allowa you to process each unique item within the

# fruits = {apple","mango", "banana"]

# # Simple for loop
# for fruit in fruits:
# printtfruit)
# # Output (order may vary - sats are unordered):
# # mango
# # apple
# # banana

# While less common, you can also use enumerate, though it doesn't offer much practical benefit for sats ghven their unordered natuna.

# # Looping with enumerate (rrely neaded for sets, but works)
# for i, fruit in enumerate(fruits, start=1):
# printr 0. (fruit"]

# Practical Application: Unique Words

# A powerful us case is estracting and processing unique items, like words from a sentence, enauring each word ia handled only once.

# # Practical use - printing only unique words from a sentence
# sentence = "python is fun and python is powerful"
# words = set[sentence.split(l

# for word in words!
# printword)
# # Output (order may vary):

# # powerful
# # fun
# # python