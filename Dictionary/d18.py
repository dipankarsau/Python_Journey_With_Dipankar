# Q92. Combine Lists into Dictionary
# You have two separate lists: one containing subject names and another containing corresponding marks. Create a dictionary from these two
# lists using dictionary comprehension, mapping each subject to its marka


subjects = ["Math", "English", "Python"]
marks = [85, 70, 95]

result={subjects[i]:marks[i] for i in  range (len(subjects))}
print(result)