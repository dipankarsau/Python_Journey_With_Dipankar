# import time
# import threading

# def task():
#     print("This task is running")

#     time.sleep(2)

#     print("Task finished\n")

# print(" main program start\n")
# t = threading.Thread(target=task)
# t.start()



# print("The program is finished\n")






import time
import threading

def task(name):
    print(f'{name}"This task is running"')

    time.sleep(2)

    print(f" {name}Task finished\n")

print(" main program start\n")
t1 = threading.Thread(target=task,args=("cooking",))
t2 = threading.Thread(target=task,args=("braking",))
t3 = threading.Thread(target=task,args=("swiming",))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()



print("The program is finished\n")