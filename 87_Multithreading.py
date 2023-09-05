import threading
import time

#Indicate some task being done
def func(second):
    print(f"Sleping for {second} seconds")
    time.sleep(second)

#Normal execution
""" time1 = time.perf_counter() #For calculate execution time start from time1
func(4)
func(1)
func(3)
time2 = time.perf_counter()#For calculate execution time end with time2
print(time2-time1) """

#Threading execution
time1 = time.perf_counter()
t1 = threading.Thread(target=func,args=[4])
t2 = threading.Thread(target=func,args=[1])
t3 = threading.Thread(target=func,args=[3])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
time2 = time.perf_counter()#For calculate execution time end with time2
print("\n",time2-time1)