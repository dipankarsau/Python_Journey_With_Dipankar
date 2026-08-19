my_tuple=(45,32,11,"anirudh","khurana","surat",99)
n=len(my_tuple)
for i in range(0,n):
    print(my_tuple[i],end=' ')

for i in my_tuple:
    print(i,end='  ')
print()


for index,value in enumerate(my_tuple):
    print(f" index={index}, value={value}")

