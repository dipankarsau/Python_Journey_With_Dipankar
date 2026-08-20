# Q84: Top Scorers
# Populate a dictionary with six student names and their corresponding
# marks. Loop through it and print the names of all students who achieved
# a score above 75.
students = {
    "Akash": 82,
    "Rahul": 68,
    "Priya": 91,
    "Amit": 74,
    "Sneha": 88,
    "Rohan": 72
}
for i,v in students.items():
    if v>=75:
        print(i)