# 84: Top Scorers Populate a dictionary with six student names and their corresponding marks. Loop through it and print the names of all students who achieved a score above 75.   also not provide only provide structure
students = {
    "Rahul": 80,
    "Amit": 65,
    "Priya": 90,
    "Suman": 72,
    "Riya": 85,
    "Arjun": 70
}

for i, v in students.items():
    if v>75:
        print(i)
