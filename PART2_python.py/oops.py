class Student:

    def __init__(self, name: str, age: int, marks: list[int]) -> None:
        self.name: str = name
        self.age: int = age
        self.marks: list[int] = marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() / len(self.marks)


student1 = Student("dipankar", 21, [78, 54, 19, 63])

print(student1.total())
print(student1.average())