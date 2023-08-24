#there aree not direct way to add anything in tupple 
#if you want to change in tupple so first you have to copy that tupple to other list 
#and change their and after that change list to tuple
#Example1:-
countries = ("Span", "italy", "India", "America", "England")
temp = list(countries)
temp.append("Russia")
#temp.pop(3) #delete an item in list
temp[2]= "Finland"
countries= tuple(temp)
print(countries) 
#Example2:- (merge two tupple to make change in tuple)
countries1 = ("India", "Shri Lanka", "Bangladesh")
countries2 = ("Chine","Nepal")
South_Asia = countries1+countries2
print(South_Asia)

#count (this show that how much occurenece are in tuple)
tup2 = (0,1,4,5,3,5,8,6,0,4,6,5,9,3,4,2)
res = tup2.count(3)
print("Countof 3 in tuple is: ", res,"times")

#index (mean it shows where first occurence is places in tuple)
res1 = tup2.index(3)
print("First occurence of 3 according to index in tuple is: ", res1)
res2 = tup2.index(3,4,8)
print("where 3 is places in between the given values according to index: ", res2)

#length
res = len(tup2)
print("Count the length of tuple: ",res)