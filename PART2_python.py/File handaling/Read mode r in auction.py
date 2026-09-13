# f=open("hello.txt","r")
# content=f.read()
# print(content)
# f.close()


# f=open("hello.txt","r")
# content=f.read(10)
# print(content)
# content1=f.read(10)
# print(content1)
# f.close()


with open("hello.txt","r") as f:
    content=f.read(10)
    print(content)