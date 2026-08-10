# return Statement
# The return statement sends a value back to whoever called the function.
# Without return, a function just does something but gives nothing back.
# With return, you can use the result in the rest of your program.

# Without return - result is lost
def add(a, b):
 print (a + b)

# With return - result can be stored and used
def add(a, b):
 return a + b

result = add(10, 5)
print(result)
print(add(3, 7) * 2)

# prints but gives nothing back

# 15
# 20
# add 3 number
def add(num1,num2,num3):
 return num1+num2+num3

print(add(2,3,4))



# true or flase return, if user can vote or not
def vote(age):
 if age>=18:
  return True
 return False

print(vote(10))
 
 