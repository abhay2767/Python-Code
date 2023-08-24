#sets are unchangeble like tuple and set will ignor duplicate items and sets are unordered.
s = {2,5,2,4,6,2,9}
print(s)
s1 = {"Abhay", 1,9,2,'Dubey', "Abhay", True}
print(s1)

#check check the class type of empty set 
s1 = {}
print(type(s1)) #This will show you that this is a Dictsnary class
s2 = set()
print(type(s2)) #So this is the right way to check the class type of set
#Having confusion because set and dictsnary are about same.

#Accessing the set item using for loop
s3 = {"Abhay", "Dubey", 1,1.2 ,True, False, 'a'}
for item in s3:
    print(item)