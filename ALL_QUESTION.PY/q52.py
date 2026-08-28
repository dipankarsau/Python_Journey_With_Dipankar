# Q60. Given two lists, merge them into a single new list without modifying the originals.

num1 = [1, 2,3]
num2 = [65, 32, 11]

def  greet(num1,num2):
    num3=[]
    for i in num1:
        if i not in num3:
            num3.append(i)
    for i in num2:
        if i not in num3:
            num3.append(i)
    return  num3
print(greet(num1,num2))

