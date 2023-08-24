#Difference between in (is) and (==)
#is:- The "is" keyword compares the exact location of object in memory
#"==":- this operator campares the value ie: like that 2 object ki value same h ya nhi
#Note:- "=" and "==" are comparison operator hote h

a = 4 #This is constant mean this is never changeble
b = 4 #This is constant mean this is never changeble
#b = "4" #this is string
print(a is b) #True
print(a == b) #True


a1 = [1,2,43] #list:- list can be changeble
b1 = [1,2,43] #list:- list can be changeble

print(a1 is b1) #False:- 
print(a1 == b1) #True:-

a2= (1,2) #tuple:- tuple is immutable mean can not changeble
b2= (1,2) #tuple:- tuple is immutable mean can not changeble

print(a2 is b2) #True
print(a2 == b2) #True

a3 = None #This will also store in memory only once and can not changeble
b3 = None #This will also store in memory only once and can not changeble

print(a3 is b3) #True
print(a3 == b3) #True