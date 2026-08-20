students = {
"101": {"name": "Rahul", "age": 21, "city": "Delhi"
        },
"102": {"name": "Priya", "age": 20, "city": "Mumbai"},
"103": {"name": "Karan", "age": 22, "city": "Pune","detail"
:{"ph":81881,"gender":"male"}},
}


# print(students["101"])
# print(students["101"]["name"])
# print(students["103"] ["name"])
# print(students["103"]["detail"]["ph"])
for a, b in students.items():
    print(f"roll_no={a}, value={b['name']}, details={b['age']}")