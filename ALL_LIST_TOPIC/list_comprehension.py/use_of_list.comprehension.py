

square=[i*i for i in range(1,11)]
print(square)



# 1to 20 , but only even number

new=[i for i in range(1,21) if i%2==0]
print(new)

# from 1 to 100 mak a list of all prime number

def is_prime(num):
    count=0
    for i in range(1,num+1):
        if i%2==0:
            count+=1
    if count==2:
        return True
    return False
new_lst=[i for i in range(1,101) if is_prime(i)]
print(new_lst)
