# Requirements

# The class should accept name and salary as parameters.

# Store salary as a private variable.

# Create an increase_salary(percent) method to increase the salary by the given percentage.

# Create a show_salary() method to display the current salary.



class Employee:
    def __init__(self , name, salary):
        self.name=name
        self.__salary=salary
    def increase_salary(self, percent):
        add=self.__salary*percent/100
        self.__salary=add+self.__salary
    def show_salary(self):
        return f" {self.__salary}"
e1=Employee("rahull",10000)
e1.increase_salary(10)
print(e1.show_salary())