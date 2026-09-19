import threading
import time
balance=1000
lock=threading.Lock()
def withdrawl(amount):
    global balance
    with lock:
        temp=balance
        time.sleep(0.001)
        balance=temp-amount


t1=threading.Thread(target=withdrawl,args=(100,))

t2=threading.Thread(target=withdrawl,args=(100,))
t1.start()
t2.start()
t1.join()
t2.join()
print(" __Bank Transfer__")
print(f" expected balance:800 -. got: {balance}")