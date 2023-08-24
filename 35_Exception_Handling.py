num = input("Enter the number to generate the multiplecation table: ")
print(f"Multiplecation table of {num} is: ")
""" for i in range(1,11):
    print(f"{int(num)}, X {i} = {int(num)*i}") """

#print("This is vary important line of the code")

#Here the problem is that when you input a number like 1,2,3,4... so on
#And other side when you insert the any kind of string ie: "Abhay" than you will see an Error.
#so here will handle that error shows that the reason of the Error.
#Big problem is that after get any Error in code. this will stop Executing other down code



#Instead of doing abobe code try to use try...except
try:
    for i in range(1,11):
        print(f"{int(num)}, X {i} = {int(num)*i}")

except Exception as e:
    print(e)
    print("Invalid input",e)

print("This is vary important line of the code")

#Some Special kind Error Handle
try: 
    num = int(input("Enter an Integer: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Please enter Integer not any thing other")
except IndexError:
    print("Please provide right Index")
print("The Square of giving number is: ", num**2)