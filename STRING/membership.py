text="programing"
# print("p"  in text)
# print("z" in text)
# print("z" not in text)
# print("m" not in text)

# total=0
# for i in text:
#     if i=="a" or i=="e" or i=="i" or i=="u" or i=="u":
#         total=total+1
# print(total)
total=0
for i in text:
    if i in "aeiouAEIOU":
        total+=1
print(total)