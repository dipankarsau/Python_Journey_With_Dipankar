# Create a tuple of marks of 6 students. Print the highest, lowest, total, and average.
marks = (75, 82, 68, 91, 55, 88)
total=0
n=len(marks)
for i in marks:
    total=total+i
average=total/n

print(max(marks), min(marks),average )
