# Q83: Subject Performance Analysis
# Given a dictionary of marks for different subjects, loop over its values()
# to calculate and print the total marks and the average mark obtained.

marks = {
    "maths": 85,
    "science": 90,
    "english": 78,
    "computer": 95,
    "history": 72
}

n = len(marks)
total = 0

for k, v in marks.items():
    total = total + v

average = total / n

print("Total Marks:", total)
print("Average Marks:", average)
