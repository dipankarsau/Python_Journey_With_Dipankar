# using a for loop
# fruit=["apple","mango","banna"]
# for i in fruit:
#     print(i)
  

# using a while lopp
fruit=["apple","mango","banna"]
i=0
while i<len(fruit):
    print(fruit[i])
    i=i+1


# looping using enumerate()
#use kora hoy jokhon value ar index duto chai

# num=[5,7,4,64,32,17,53,85,3,1,999]
# for index,value in enumerate(num):
#     print(f' index value is {index}value is {value}')

    # even number ar index print
num = [5, 7, 4, 64, 32, 17, 53, 85, 3, 1, 999]

for i, v in enumerate(num):
    if v % 2 == 0:
        print(i)