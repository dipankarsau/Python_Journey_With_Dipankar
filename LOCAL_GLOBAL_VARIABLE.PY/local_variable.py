# Scope refers to where a variable is accessible in your code. A variable created
# inside a function is local it only exists inside that function. A variable created
# outside all functions is global it can be accessed from anywhere.


def addition(n1,n2,n3):
    total=n1+n2+n3
    print(f" the total is {total}")

addition(10,20,30)



def xyz(n1, n2):
 n1 = 100
 n2 = 200
 print(f"Inside function n1={n1}.and n2={n2}")

n1 = 10
n2 = 20
xyz(n1, n2)
print(n1)
print(n2)