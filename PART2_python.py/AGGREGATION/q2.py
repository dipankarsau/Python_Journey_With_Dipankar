# Department and Employee Management


class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.__salary=salary
    def show_details(self):
        print(self.name)
        print(self.__salary)
class Department:
    def __init__(self, depart_name, employee):
        self.depart_name=depart_name
        self.employee=employee
    def show_department(self):
        print(self.depart_name)
        self.employee.show_details()
E1=Employee("rahul", 25000)
d1=Department("IT", E1)
d1.show_department()