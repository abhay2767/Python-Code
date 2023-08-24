#map()
cube = lambda x: x*x*x
print(cube(5))

#Just double each number of the list using map() function
lst = [1, 2, 3 ,4 ,5]
#1st way:-
newlst = []
for item in lst:
    newlst.append(cube(item))
print("Using for loop: ",newlst)

#2nd way:-
""" newlst1 = map(cube, lst)
#now typecast in list because this will return value in map
a =list(newlst1)
print("Using map() function: ",a) """
#or
newlst1 = list(map(cube, lst)) #By default this will return map object and we want in list object
#so here we typecast that from map to list using list keyword
print("Using map() function: ",newlst1)
#or using lambda
newl = list(map(lambda x: x*x*x, lst))
print("Map using lambda function: ",newl)


#filter()
def filter_function(a):
    return a>4 #This will return in boolean True or False
newlst2 = filter(filter_function, lst) #Again this will return or give value in filter object
#Again we have to typecast this in list 
b = list(newlst2)
print(b) #Here this return 5 because list me 4 se bda only ek hi element h (5)

#reduce()
from functools import reduce

#list of number
num = [1,2,3,4,5]
#calculate the sum of the numbers using reduce function
#1st way using lambda function
sum = reduce(lambda x, y : x+y, num)
print("sum using Reduce Function: ",sum)

#2nd way: 
def sum1(a,b):
    return a+b
sum2 = reduce(sum1,num)
print("sum in different way using Reduce Function: ",sum2)