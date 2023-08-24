x = 4 #Global variable x

def hello():
    y = 5;  #Local varible y
    print("The Local x is: ",{x})
    #Local variable are destroyed as soon as your function returns
    print("Hello, Abhay")

print("The Global x is: ",{x})
hello()
#print("The Local x from function is: ",{y}) #This will not print shows an Error """

#Because we can not access any functions Local variable outside 
#but there is a way to change value of Global variable inside function
#way is:
txt = "Abhay"

def text():
    global txt
    print("Before ",txt)
    txt = "Dubey"
    print("After ",txt)

text()
print("Ouside the function ",txt)