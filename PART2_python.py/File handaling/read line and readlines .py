# with open("hello.txt","r") as f:
#     line1=f.readline()
#     print(line1 .strip())
#     line2=f.readline()
#     print(line2.strip())

with open("hello.txt","r") as f:
    line1=f.readlines()
    print(line1)
    for line in line1:
        print(line.strip())