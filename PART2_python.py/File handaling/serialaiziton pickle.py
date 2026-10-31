class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        return (f" name={self.name}, age={self.age}")
P=person("aksh", 21)

import pickle
with open(" person.pickle", "wb") as f:
    pickle.dump(P,f)


import pickle
with open("C:/Users/Dipankar/Documents/Demo_Python/Python_Journey_With_Dipankar/PART2_python.py/File handaling/ person.pickle","rb")as f:
    print(pickle.load(f))
    print(P.display())
    