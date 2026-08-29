# Q92. Combine Lists into Dictionary
# You have two separate lists: one containing subject names and another conta

subjects = ["math", "science", "english", "computer", "history"]

marks = [85, 92, 78, 95, 88]
new=dict(zip(subjects,marks))
print(new)