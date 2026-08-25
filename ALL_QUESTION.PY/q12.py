# Take a person
# '
# s age and whether they have a valid ID (True/False) as input. They
# can enter a venue only if they are 18 or older AND have a valid ID. Print the
# appropriate message.




user=int(input('enter your age:-'))
id=input("you have a valid id  (True /Flase) :")
if user>=18 and id=="True":
    print("you are eligible for vote")
else:
    print('you are not eligible for vote')