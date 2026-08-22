# Q86. Subjects and Marks
# Create a dictionary of 6 subjects and their respective marks. Print the subject
# with the highest marks and the one with the lowest, using max() and min()
# functions alongside a lambda expression.


subjects = {
    "Math": 85,
    "English": 72,
    "Python": 95,
    "DBMS": 80,
    "Java": 88,
    "Computer": 76
}
highest=max(subjects,key=lambda x:subjects[x])
smallest=min(subjects,key=lambda x:subjects[x])

print(highest,smallest)