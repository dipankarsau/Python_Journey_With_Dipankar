class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"name = {self.name}, age = {self.age}")

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "B+"
        elif avg >= 60:
            return "C"
        else:
            return "D"


Student1 = Student("akash", 22, [20, 34, 56, 78])

Student1.display()
print(Student1.average())
print(Student1.grade())