#when you pass function as an argument that time you can use lambda function
#1st way:-
def double(x): #A dunction to double the input value
    return x * 2 
print(double(9))

#2nd way:- using lambda function
doubles = lambda x: x*5 #Single argument
cube = lambda x: x*x*x 
avg = lambda x,y:(x+y)/2 #double argument
avg1 = lambda x,y,z:(x+y+z)/2 #double argument
print(doubles(5))
print(cube(2))
print(avg(4,6))
print(avg1(4,6,8))

#You can pass the function to function
def apple(fx, value):
    return 6 + fx(value)
print(apple(cube,2))

#Note: Working of both function are same, use according to requirement or use in small functios 