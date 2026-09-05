class Student:
    name = ""
    age = 0
    gender = ""
    roll_no = ""

    def set_details(self, name: str, roll_no: str, age: int, gender: str):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.gender = gender

    def display_details(self):
        print(f"name = {self.name}")
        print(f"roll_no = {self.roll_no}")
        print(f"age = {self.age}")
        print(f"gender = {self.gender}")


Student1 = Student()  

Student1.set_details("akash", "1", 23, "male")
Student1.display_details()

    