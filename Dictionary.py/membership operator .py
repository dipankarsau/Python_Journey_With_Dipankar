student={
  "name":"rahul",
  "age":35,
  "gender":"male",
  "city":"surat"



}
# print("age" in student)
# print(35 in student)
k=input("enter what you want")
if k in student:
    print(student[k])
else:
    print(" key does not exit")
