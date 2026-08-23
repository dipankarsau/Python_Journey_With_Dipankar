# 13. Strings in Python > 10. String Methods - Splitting and Joining.py > ...

# String Methods: Splitting and Joining
# split(): Break String into List
# join(): Combine List into String


# text="anirudh khurana is a coder"
# print(list(text))
# print(text.split())
# print(text.split("a"))


# my_list=["a","n","i","r","u","d","h"]
# print(" ".join(my_list))
my_list=["a","n","i","r","u","d","h",5]
ans="".join(str(i) for i in my_list)
print(ans)