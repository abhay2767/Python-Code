#List item can store multiple item in single variable and list can be changeble
#List are mutable(changeble)
list1 = [1,3,5,2,8,6,5]
list2 = ["Red", "Blue", "Green"]
list3 =[1,3,"Abhay"] #In list we can be different different datatype in single varible
print(type(list1))

#find given number is avaible in list or not
if 6 in list1:
    print("Yes it is avialble")
else:
    print("Not  avialble")

if "Red" in list2:
    print("Yes it is avialble")
else:
    print("Not  avialble")

#same thing apply for string
if "bh" in "Abhay":
    print("Yes")

#print all number
print(list1)
print(list1[:]) #Here python will asume 0 at first and length of list  so (0:6)
print(list1[1:-1]) # mean length is 7 so 7-1 = 6 tak jayega and it start from 1
print(list1[1:6:2]) #jumping to 2 index here 1 to 7 slicing



print("list1 is ",list1)
print(list1[0])
print(list1[1])

print("Negative indexing: ",list1[-3]) #Negative indexing total index  - given number 
print("Negative indexing: ",list1[len(list1)-3]) # (7-3) = 4 mean print the 4th postion number 


print("list2 is ",list2)
print(list2[1])
print(list2[0])

print("list3 is: ",list3)
print(list3[2])
print(list3[1])

#List comprehensive (generate list by given range)
list3 = [i for i in range(5)] #Expression element ban jayega
print(list3)

list3 = [i*i for i in range(10) if i%2==0] 
print(list3)
