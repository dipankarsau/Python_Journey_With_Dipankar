
class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.__salary = salary

    def getter(self):
        return self.__salary

    def show_details(self):
        print(self.employee_id, self.name, self.getter())

    def update_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid Salary")


class Department:
    def __init__(self, depart_name):
        self.depart_name = depart_name
        self.employee = []

    def add_employee(self, employee):
        self.employee.append(employee)

    def remove_employee(self, employee_id):
        for emp in self.employee:
            if emp.employee_id == employee_id:
                self.employee.remove(emp)
                print("Employee Removed")
                return

        print("Employee Not Found")

    def show_employee(self):
        print("Department:", self.depart_name)

        for emp in self.employee:
            emp.show_details()


e = Employee(4, "akash", 20000)
d = Department("cse")

d.add_employee(e)
d.show_employee()

d.remove_employee(4)
d.show_employee()
