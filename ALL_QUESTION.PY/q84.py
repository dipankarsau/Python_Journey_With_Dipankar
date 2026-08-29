# Q87. Student Details
# Create a nested dictionary containing details for 4 students, where each
# student entry includes their name, age, and city. Write a loop to print the full
# details of each student in a clear, readable format.
students = {
    "student1": {
        "name": "Rahul",
        "age": 20,
        "city": "Kolkata"
    },
    "student2": {
        "name": "Priya",
        "age": 21,
        "city": "Delhi"
    },
    "student3": {
        "name": "Amit",
        "age": 19,
        "city": "Mumbai"
    },
    "student4": {
        "name": "Sneha",
        "age": 20,
        "city": "Chennai"
    }
}

for i, v in students.items():
    print(f"Details of {i}: Name = {v['name']}, Age = {v['age']}, City = {v['city']}")