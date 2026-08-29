# Q86. Subjects and Marks Create a dictionary of 6 subjects and their respective marks. Print the subject with the highest marks and the one with the lowest, using max() and min() functions alongside a lambda expression.    provide srtucture not answer\
marks = {
    "math": 85,
    "science": 92,
    "english": 60,
    "hindi": 45,
    "computer": 95,
    "history": 70
}
a = dict([max(marks.items(), key=lambda x: x[1])])

print(a)
b=dict([min(marks.items(), key=lambda x: x[1])])
print(b)