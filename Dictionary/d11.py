# Q87. Student Details
# Create a nested dictionary containing details for 4 students, where each
# student entry includes their name, age, and city. Write a loop to print the full
# details of each student in a clear, readable format.
students = {
    "student1": {
        "name": "Akash",
        "age": 21,
        "city": "Kolkata"
    },

    "student2": {
        "name": "Rahul",
        "age": 22,
        "city": "Delhi"
    },

    "student3": {
        "name": "Amit",
        "age": 20,
        "city": "Mumbai"
    },

    "student4": {
        "name": "Riya",
        "age": 23,
        "city": "Pune"
    }
}
for i,v in students.items():
    print(i,v)