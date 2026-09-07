class Student():
    scholol="bara bari sri krishna high school"
    def __init__(self,name:str):
        self.name=name
    def display(self):
     print(self.name)

s1=Student("akash")
s2=Student("goru")
s1.display() # instance variable
s2.display() # instance variable
print(s1.scholol)   # class variable
# 1st way to change class variable
print(Student.scholol)  
s1.scholol="xyz"
print(s1.scholol) # class variable