#This will alway execute code this is use at end of try... except... finally.. just like Else
try:
    lis = [1,5,6,2,9,7]
    ind = int(input("Please enter index number to view value: "))
    print("Value of index is: ",lis[ind])
except:
    print("There are some Error Occur while providing Index Number")
finally:
    print("😎Duniya jaye bhad me mujhe execute hone h bas😎")
    #or
print("😎Duniya jaye bhad me mujhe execute hone h bas😎")

#Big Question: Why is finally needed because we can print or execcute code 
# like just to write the code outside from try..except..
#Ans: Right!, but when you use this in any Function than your second way will not work
#ie:-
def squar():
    try:
        n = int(input("Enter Number: "))
        print("Squar of num is: ",n**2)
        return 1
    except:
        print("Invalid input")
        return 0
    finally:
        print("Abhi bhi M print hokar rahunga")
    print("😎Duniya jaye bhad me mujhe execute hone h bas😎")
x = squar()
print(x)