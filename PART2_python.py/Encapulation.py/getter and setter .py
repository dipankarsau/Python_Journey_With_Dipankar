class Student:
    def __init__(self, name: str):
        self.__name = name

    # getter
    def get_name(self):
        return self.__name

    # setter
    def set_name(self, new_name: str):
        self.__name = new_name


s1 = Student("akash")

print(s1.get_name())

s1.set_name("dipp")

print(s1.get_name())