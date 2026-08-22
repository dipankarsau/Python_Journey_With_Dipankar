# Q88. Student Marks Analysis
# Design a dictionary where each key is a student's name and the
# corresponding value is a list of their marks in 3 different subjects. Calculate
# and print the total marks and average marks for each student


students = {
    "Akash": [85, 90, 78],
    "Rahul": [70, 65, 80],
    "Amit": [95, 88, 92],
    "Riya": [75, 82, 79]
}

for i, v in students.items():
    n = len(v)
    total = sum(v)
    average = total / n

    print(f"Student: {i}")
    print(f"Total: {total}")
    print(f"Average: {average}")