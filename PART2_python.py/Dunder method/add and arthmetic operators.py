# class Distance:
#     def __init__(self,km):
#         self.km=km
#     def __add__(self, other):
#         return  self.km+other.km
#     def __mul__(self, other):
#         return self.km*other
#     def __sub__(self,other):
#         return self.km-other.km
    
    

# d2=Distance(30)
# d1=Distance(40)
# print(d1+d2)
# print(d1*3)
# print(d2-d1)


class Fraction:
    def __init__(self, x, y):
        self.num = x
        self.den = y

    def __add__(self, other):
        num_1 = self.num * other.den + self.den * other.num
        num_2 = self.den * other.den

        return f"{num_1}/{num_2}"

    def __sub__(self, other):
        num_1 = self.num * other.den - self.den * other.num
        num_2 = self.den * other.den

        return f"{num_1}/{num_2}"

    def __mul__(self, other):
        num_1 = self.num * other.num
        num_2 = self.den * other.den

        return f"{num_1}/{num_2}"
    def decimal_convert(self):
        return self.num/self.den


fr1 = Fraction(3, 4)
fr2 = Fraction(1, 2)

print("Addition:", fr1 + fr2)
print("Subtraction:", fr1 - fr2)
print("Multiplication:", fr1 * fr2)
print(fr1.decimal_convert())