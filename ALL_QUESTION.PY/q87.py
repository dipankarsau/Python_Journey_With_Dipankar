# Q90. Numbers to Cubes
# Using dictionary comprehension, create a new dictionary where keys are numbers from 1 to 10 (inclusive), and values are the cube of each
# numbe
new={i:i*i*i for i in range(1,11)}
print(new)