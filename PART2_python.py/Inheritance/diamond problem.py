class A:
    def hello(self):
        print("A")
class B:
    # def hello(self):
    #     print("B")
    pass
class c:
    # def hello(self):
    #     print("C")
    pass
class D(B,c,A):
    # def hello(self):
    #     print("D")
    pass
d1=D()
d1.hello()
print(D.__mro__)