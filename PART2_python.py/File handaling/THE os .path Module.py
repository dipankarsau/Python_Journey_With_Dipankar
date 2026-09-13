import os
print(os.path.exists("new.text"))
print(os.path.isfile("new.text"))
print(os.path.getsize("new.txt"))
path=os.path.join("data","logs","app.log")
print(path)