# Create a dictionary containing the names and salaries of 6 employees. Use sorted() along with a lambda expression to sort the employees by salary in descending order. Then, print only the top 3 highest-paid employees along with their salaries.
employees = {
    "Akash": 35000,
    "Rahul": 28000,
    "Amit": 45000,
    "Riya": 32000,
    "Suman": 50000,
    "Karan": 40000
}
result=sorted(employees .items(),key=lambda x:x[1],reverse=True)
print(result[:3])