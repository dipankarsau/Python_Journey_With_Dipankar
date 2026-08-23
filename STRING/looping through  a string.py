name="python"
n=len(name)
# using for loop
for i in name:
    print(i)

for i,v in enumerate(name):
    print(i,v,end =' ')
for i in range(0,n):
    print(name[i])

# using while loop
i=0
while i<n:
    print(name[i])
    i=i+1