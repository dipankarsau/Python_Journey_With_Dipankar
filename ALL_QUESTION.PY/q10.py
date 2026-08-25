#  Take a student'
# s marks as input. Print their grade based on this scale:
# 90 and above → A
# 75 to 89 → B
# 60 to 74 → C
# 40 to 59 → D
# Below 40 → F



student=int(input('enter student mark'))
if student >=90:
    print("a")
elif student>=75 and student<=89:
    print("b")
elif student>=60 and student<=74:
    print("c")
elif student>=40 and student<=59:
    print("d")
else:

    print("f")