#some time we have to raise a custor error to stop the execution of code 
#Khud se Error raise karna: kyunki koi unexpected na ho
a = int(input("Enter any value form 5 to 10: "))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")


salary = int(input("Enter salry: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")


#Defining Custom Excepton
class CustomError(Exception):
    #code
    pass
try:
    i = int(input("Inter Number: "))
    print(i*i)
except:
    print("Hello Guys")

#Quiz: 
n = input("Enter Quit to enter in If condtion: ")
out = "Quit"
raise ValueError("Please provide right input")
#If user provide wrong input than this will stop the execution of the code here
#This will not go neither in If nor Else blcok
if(n == out):
    print("Wellcome, Abhay Dubey")
else:
    print("Better Luck next timeṇ")