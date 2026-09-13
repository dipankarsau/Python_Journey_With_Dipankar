import os
from pathlib import Path


# os.rmdir("new_folder")
# os.rmdir("new_folder1")
# os.mkdir("new_folder")
# # os.remove(new1.txt)
# os.rename("new.txt","new.txt1")
# # Show all files and folders
# for f in os.listdir("."):
#     print(f)
for f in Path("C:\\").iterdir():
    print(f)