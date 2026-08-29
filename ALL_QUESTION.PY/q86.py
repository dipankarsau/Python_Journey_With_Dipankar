# Q89. Top 3 Subjects by Marks
# Given a dictionary of subjects and their marks, sort it by marks in descending
# order. Then, print only the top 3 subjects with the highest marks.


marks = {
    "math": 85,
    "science": 92,
    "english": 78,
    "computer": 95,
    "history": 88,
    "geography": 70
}
a=sorted(marks.items(), key=lambda x: x[1] ,reverse=True)


for i,v in  a[:3]:
    print(i,v)
    
   