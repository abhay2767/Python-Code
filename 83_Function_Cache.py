import functools
import time

#First Example:-
@functools.lru_cache(maxsize=None)
def fib(n):
    if(n < 2):
        return n
    return fib(n-1)+ fib(n-2)

print(fib(20))

#Another example:-
@functools.lru_cache(maxsize=None)
def fun(n):
    time.sleep(5)
    return n*5

print(fun(20))
print("Done for 20")
print(fun(10))
print("Done for 10")
print(fun(30))
print("Done for 30")

#This will print fast
print(fun(20))
print("Done for 20")
print(fun(10))
print("Done for 10")
print(fun(30))
print("Done for 30")

#This will compute again because this is new value
print(fun(50))
print("Done for 50")