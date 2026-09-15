from datetime import datetime
now=datetime.now()
print(now)


from datetime import date
today=date.today()
print(today)




from datetime import date, timedelta

x= date.today() + timedelta(days=1)
print(x)




from datetime import date, timedelta
x=date.today()-timedelta(days=1)
print(x)


