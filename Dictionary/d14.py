# Create a dictionary containing the names and marks of 6 students. Use sorted() along with a lambda expression to sort the students by their marks in descending order. Then, print only the top 3 students along with their marks.

students = {
    "Akash": 85,
    "Rahul": 45,
    "Amit": 90,
    "Riya": 72,
    "Suman": 95,
    "Karan": 80
}
result=sorted(students.items(), key=lambda x: x[1], reverse=True)
print(result[:3])
