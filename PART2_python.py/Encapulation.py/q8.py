# Create a class called Employee to manage employee salary.


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid Salary")

    def increase_salary(self, percentage):
        add = self.__salary * percentage / 100
        self.__salary = self.__salary + add


E = Employee("Rahul", 20000)

print(E.get_salary())

E.increase_salary(10)
print(E.get_salary())

E.set_salary(25000)
print(E.get_salary())

E.set_salary(-5000)

   
    

