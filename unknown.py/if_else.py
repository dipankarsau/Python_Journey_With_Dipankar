# age=int(input("enter a number"))
# if age>=18 and age<=60:
#     print(f"you are eligible for vote{age}")
# else:
#     print(f"you are  not eligible fot vote {age}")
    # question
#     90 above -> A
# 81 - 90 -> B
# 71 - 80 -> C
# 61 - 70 -> D
# 60 and below -> Fail
marks=int(input('enter a number'))
if marks>=90:
    print(f"grade A you number is {marks}")
elif marks>=81 and marks<=90:
    print(f"grade A you number is {marks}")
elif marks>=71 and marks<=80:
    print(f"grade A you number is {marks}")
elif marks>=61 and marks<=70:
    print(f"grade A you number is {marks}")
else:
    print(f"your are fail {marks}")