#Decorator is modify a function
def greet(fx):
    def mfx(*arg, **koarg): #This is the way to take argument if the arument not getting
        #  *arg:- this will take argument as tuple
        #  **koarg:- this will take argument as dictinary
        print("Good Morning")
        fx(*arg, **koarg)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World")

@greet
def add(a,b):
    print("Addition is: ",a+b)

def sub(a,b):
    print("Substraction is: ",a-b)


hello()
#greet(add)(1,2) #The argument will not reach to add function
add(1,2)
sub(5,3)