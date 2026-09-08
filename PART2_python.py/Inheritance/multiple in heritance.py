class Flyer:
    def fly(self):
        print("flying")

class Swimmer:
    def swim(self):
        print("swiming")
class Duck(Flyer,Swimmer):
    def quack(self):
        print("QUACK")
c=Duck()
c.fly()
c.swim()
c.quack()