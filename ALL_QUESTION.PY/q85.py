# Student Marks Analysis
# Design a dictionary where each key is a student's name and the
# corresponding value is a list of their marks in 3 different subjects. Calculate
# and print the total marks and average marks for each student.
students = {
    "Rahul": [80, 75, 90],
    "Priya": [85, 92, 88],
    "Amit": [70, 65, 78],
    "Sneha": [95, 90, 85]
}
for i, v in students.items():
    a = sum(v)
    n = len(v)
    avg = a / n

    print(i, "Total =", a, "Average =", avg)
   