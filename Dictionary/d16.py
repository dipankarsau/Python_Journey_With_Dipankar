
# Q90. Numbers to Cubes Using dictionary comprehension, create a new dictionary where keys are numbers from 1 to 10 (inclusive), and values are the cube of each number.   


number = range(1, 11)

result = {x: x**3 for x in number}

print(result)