import time
#time.time():-
""" def usingwhile():
    i = 0
    while i<50000:
        i = i+1
        print(i)
def usingfor():
    for i in range(50000):
        print(i)

init = time.time()
usingfor()
t1 = time.time()-init
init = time.time()
usingwhile()
print(t1)
print(time.time()-init) """


#time.sleep():-
print(4)
time.sleep(3)
print("Thsis will print after 3 sec")

#time.strftime():-
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)