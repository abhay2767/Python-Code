a = input("Enter your Name: ");
print("My name is: ",a);

#This will take the user input as a String  by default
a = input("Enter First Number ");
b = input("Enter Secand Number ");
print("Addion as string ", a+b)

#Now we have to typecast of the data type
a = int(input("Enter First Number "));
b = int(input("Enter Secand Number "));
print("Addion as Number", a+b)
 
#Another Way to typecast datatype
a = input("Enter First Number ");
b = input("Enter Secand Number ");
print("Addion as string ", int(a)+int(b));
