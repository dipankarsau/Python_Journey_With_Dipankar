# Q91. Filter Passing Marks
# Given an existing dictionary of subjects and their respective marks, use dictionary comprehension to generate a new dictionary that includes
# only the subjects where the student scored 40 or more (i.e., passed

marks = {
    "math": 85,
    "science": 35,
    "english": 60,
    "hindi": 28,
    "computer": 75,
    "history": 40
}
new={i:v for i,v in marks.items() if v>=40}
print(new)