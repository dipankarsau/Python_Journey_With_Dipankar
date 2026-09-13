try:
    f = open("data.txt", "r")
    content = f.read()

except FileNotFoundError:
    print("File not found.")

else:
    print(content)

finally:
    print("Cleanup completed.")