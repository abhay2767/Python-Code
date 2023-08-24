"""
Function Argument:-
    1- Default Argument
    2- Keyword Argument
    3- Variable length Argument
    4- Required Argument
"""
#Required Argument:- (you have to give the value in required argument)
def average(a,b):
    print("Required Argument Average is: ",(a+b)/2)

average(4,5)

#Default Argument:-
def average(a=4,b=10):
    print("Default Argument Average is: ",(a+b)/2)

average()

def average(a=4,b=10):
    print("Default Argument Average is: ",(a+b)/2)

average(5,20)

def average(a=4,b=10):
    print("Default Argument Average is: ",(a+b)/2)

#average(5)
average(b=20)

#Keyword Argument:- (if you want to not follow order of argument)
def average(a,b):
    print("Keyword Argument Average is: ",(a+b)/2)

average(b = 20, a = 36)

#Variable length Argument:-
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
        #print("Variable length Argument Average is: ",sum/len(numbers))
        #return 7
        return sum / len(numbers)

#average(5,6)
c= average(5,6,9)
print(c)


def name(**Nam):
    print(type(Nam))
    print("Hello, ",Nam["fnam"], Nam["mnam"], Nam["lnam"])

name(mnam = "Kumar", fnam = "Abhay", lnam = "Dubey")