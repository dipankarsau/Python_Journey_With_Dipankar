# Q89. Top 3 Subjects by Marks
# Given a dictionary of subjects and their marks, sort it by marks in descending
# order. Then, print only the top 3 subjects with the highest marks.


subjects = {
    "Math": 85,
    "English": 72,
    "Python": 95,
    "DBMS": 80,
    "Java": 88,
    "Computer": 76
}
result = sorted(subjects, key=lambda x: subjects[x], reverse=True)
print(result)
