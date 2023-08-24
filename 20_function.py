#First way repeat multple time
a = 10;
b = 20;
Geo_mean = (a*b)/(a+b)
print("Geometric mean is: ",Geo_mean)

a = 30;
b = 50;
Geo_mean = (a*b)/(a+b)
print("Geometric mean is: ",Geo_mean)

#Second way using function
#User Defind function:-
def mean(a,b):
    Geo_mean = (a*b)/(a+b)
    print("Geometric mean is through function: ",Geo_mean)

#a = 10
#b = 20
a = int(input("Enter First Number "))
b = int(input("Enter Second Number "))
mean(a,b)

#Another function
def Is_Greater(a,b):
    a = int(input("Enter First Number "))
    b = int(input("Enter Second Number "))
    if(a > b):
        print("First number is greater")
    elif(a == b):
        print("Both Numbers are same")
    else:
        print("Second number is greater")

Is_Greater(a,b)

#Third function
def average(a,b):
    print("Average is: ",(a+b)/2)

average(4,5)