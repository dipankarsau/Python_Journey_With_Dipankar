# class Student:
#     # attribute
#     name=" "
#     roll_no= 0
#     age=0
#     def set_details(self):
#         self.roll_no=int(input(" enter your rool no:"))
#         self.name=input(" enter your name:")
#         self.age=int(input(" enter your age:"))
#     def display(self):
#         print(self.roll_no)
#         print(self.name)
#         print(self.age)
# Student1=Student()
# Student1.set_details()
# Student1.display()
# class Student:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age

#     @property
#     def get(self):
#         return self.__age
#     def set(self,new_age):
#         self.__age=new_age
# student1 = Student("Dipankar", 21)
# print(student1.get)
# student1.set=20
# print(student1.set)