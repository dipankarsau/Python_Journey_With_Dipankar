class Student:
    def __init__(self,rollno:int,name:str,age:int,sec:str):
        self.roll_no=rollno
        self.name=name
        self.age=age
        self.sec=sec
   
    def display_details(self):
        print(f"name = {self.name}")
        print(f"roll_no = {self.roll_no}")
        print(f"age = {self.age}")
        print(f"gender = {self.sec}")


Student1 = Student(21,"akash",22,"h")  

Student1.display_details()

    