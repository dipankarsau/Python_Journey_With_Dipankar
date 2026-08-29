# Q83: Subject Performance Analysis
# Given a dictionary of marks for different subjects, loop over its values() to calculate
# and print the total marks and the average mark obtained.


marks = {
    "maths": 90,
    "science": 85,
    "english": 88,
    "computer": 95,
    "history": 80
}
n=len(marks)
total=0
for i in marks.values():
    total=total+i
avg=total/n
print(total,avg)