# Employee Payroll Management System

class Employee:
    count=0
    def __init__(self, employee_id, name, basic_Salary):
        self.employee_id=employee_id
        self.name=name
        self.__basic_salary=basic_Salary
        Employee.count+=1
    def calculate_salary(self):
        return self.__basic_salary
    def show_salary(self):
        print(self.name)
        print(self.calculate_salary())
        print(self.employee_id)
class Manager(Employee):
    def __init__(self, employee_id, name, basic_salary,  bonus):
        super().__init__(employee_id, name, basic_salary)
        self.bonus=bonus
    def calculate_salary(self):
        return super().calculate_salary()+self.bonus
    def  show_details(self):
        print(self.employee_id)
        print(self.name)
        print(self.calculate_salary())
        print(self.bonus)
m1=Manager(102, "Amit", 50000, 10000)
print(m1.calculate_salary())
m1.show_details()