try:

    with open("hello.txt","r") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print(" file does not exit")
except:
    print(" some error occured")
