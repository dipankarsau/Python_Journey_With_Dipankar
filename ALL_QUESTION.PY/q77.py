# Safe Subject Access (HW)
# Define a dictionary with five subjects and their respective marks. Utilize the
# get() method to try accessing a subject
marks = {
    "maths": 90,
    "science": 85,
    "english": 88,
    "computer": 95,
    "history": 80
}
print(marks.get("maths"))
print(marks.get("physics"))
print(marks.get("physics", 0))