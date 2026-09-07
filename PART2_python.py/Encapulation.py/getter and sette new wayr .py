class Student:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name:str):
        self.__name=new_name
    



s1 = Student("akash")
print(s1.name)
s1.name="xyz"
print(s1.name)
