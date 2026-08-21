# Define a dictionary with five subjects and their respective marks.
# Utilize the get() method to try accessing a subject that is not in the
# dictionary, ensuring it prints "Not Available" as a default.


subjects = {
    "maths": 90,
    "science": 85,
    "english": 78,
    "computer": 95,
    "history": 70
}
print(subjects.get("geography","not avilabel"))
