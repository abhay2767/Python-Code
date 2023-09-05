import threading
import time
from concurrent.futures import ThreadPoolExecutor

#Indicate some task being done
def func(second):
    print(f"Sleping for {second} seconds")
    time.sleep(second)
    return second

def main():
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

def poolingDemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        #first way in "ThreadPoolExecutor"
        """ future1 = executor.submit(func,3)
        future2 = executor.submit(func,2)
        future3 = executor.submit(func,4)
        print(future1.result())
        print(future2.result())
        print(future3.result()) """

        #second way in "ThreadPoolExecutor" for parrallel execution
        l = [3,5,2,1]
        results = executor.map(func,l)
        for result in results:
            print("\n",result)



poolingDemo()