class animal:
    def breath(self):
        print("breathing")
class mamal (animal):
    def feedoung(self):
        print("fedding")
class dog(mamal):
    def bark(self):
        print("woof")
c=dog()
c.breath()
c.feedoung()
c.bark()
    
   