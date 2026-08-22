# Q91. Filter Passing Marks
# Given an existing dictionary of subjects and their respective marks, use dictionary comprehension to generate a new dictionary that includes
# only the subjects where the student scored 40 or more (i.e., passed)

subjects = {
    "Math": 85,
    "English": 35,
    "Python": 95,
    "DBMS": 40,
    "Java": 28,
    "Computer": 76
}
subjects = {
    "Math": 85,
    "English": 35,
    "Python": 95,
    "DBMS": 40,
    "Java": 28,
    "Computer": 76
}

result = {key: value for key, value in subjects.items() if value >= 40}

print(result)

