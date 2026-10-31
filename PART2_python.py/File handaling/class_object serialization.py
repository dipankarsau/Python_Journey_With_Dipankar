class Person:
    def __init__(self, name, lname, age, gender):
        self.name=name
        self.lname=lname
        self.age=age
        self.gender=gender
person=Person(" akash", " sau", 21, " ,male")
import json

with open("partic.json", "w") as f:
    def show(person):
        return (f" farst_name={person.name,person.lname,person.age,person.gender}")
    json.dump(person,f,default=show)