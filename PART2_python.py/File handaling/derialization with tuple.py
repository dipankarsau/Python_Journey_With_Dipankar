import json
with open("C:/Users/Dipankar/Documents/Demo_Python/Python_Journey_With_Dipankar/PART2_python.py/File handaling/ demo1.json", "r") as f:
    d=json.load(f)
    print(d)
    print(type(d))