# Employee Payroll Management System
class Employee:
    __employee_coiunt=1
    
            
    
    def __init__(self,employee_id, name , baisc_salary, department):
        self. employee_id=employee_id
        self.name=name
        self.__basic_salary=baisc_salary
        self.department=department
        self.count=Employee.__employee_coiunt
        Employee.__employee_coiunt+=1
                
        
    def calculate_salary(self):
        hra=20*self.__basic_salary/100
        da=10*self.__basic_salary/100
        tax=5*self.__basic_salary/100
        final_salary=self.__basic_salary+hra+da-tax
        return final_salary
    def give_raise(self, amount):
        if amount>0:
            self.__basic_salary=self.__basic_salary+amount
        else:
            print(" invalid raise amount")
    def transfer_department(self, new_department):
        if not new_department.strip():
            print(" invalid department")   
        else:
            self.department=new_department.strip()    
    def show_details( self):
        print(self.name)
        print(self.department)
        print(self.employee_id)
        print(self.__basic_salary)
        print(self.calculate_salary())

e=Employee(22, "ram",10000," ")
e1=Employee(21, " ve",122, " se")
print(e.calculate_salary())
e.give_raise(2000)
e.transfer_department("vbvb")
e.show_details()
print(Employee.employee_coiunt)
    


    
    




