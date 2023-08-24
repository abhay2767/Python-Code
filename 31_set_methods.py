#Sets Methods:
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
print(s1.union(s2)) #Union of both set mean all item of both set or combinatopn of both set

s1.update(s2) #Sometimes when we want to update the sets by given set name
print(s1,s2)

cities1  = {"Tokyo", "Berlin","Delhi","Kanpur"}
cities2 = {"Kanpur", "Lucknow", "Alahabad"}
cities3 = cities1.union(cities2) #Union Mean combination of both set
cities4 = cities1.intersection(cities1) #Intersaction mean comman between both set
cities4 = cities1.intersection_update(cities1) #Update the intersaction
print(cities3)
print(cities4)


cities5  = {"Tokyo", "Berlin","Delhi","Kanpur"}
cities6 = {"Kanpur", "Lucknow", "Alahabad","Tokyo"}
cities7 = cities5.symmetric_difference(cities6) #Remove the data itme which are common in set
print(cities7)

#isdisjoint (True when there are no duplicate item in each set else False)
""" 
The isdisjoint method checks if the item of given set are present in another set.
this method return False if item are present, else it return true """
cities8  = { "Berlin","Delhi","Kanpur"} #"Kanpur" = false
cities9 = { "Lucknow", "Alahabad","Tokyo"}
print(cities8.isdisjoint(cities9))

#isuperset (superset means that contains all item of set1 are present in set2)
""" The issuperset method checks if all the item of a particular set are present 
    in the original set. it return True if all the item are present, else False
 """
cities10  = {"Tokyo", "Berlin","Delhi","Kanpur"}
cities11 = {"Lucknow", "Alahabad"}
print(cities10.issuperset(cities11))
cities12 ={"Nagpur", "Lucknow","Tokyo", "Berlin","Delhi","Kanpur"}
print(cities12.issuperset(cities10))


#issubset ()
""" The issubset method checks if all the item of the original set are present in the
    particular set. It return True if all the item are present, Else false
 """
cities13  = {"Tokyo", "Berlin","Delhi","Kanpur"}
cities14 = {"Lucknow", "Alahabad"}
cities15 ={"Tokyo", "Berlin"}
print(cities10.issubset(cities12))

#add (if yu want to add a single item to the set use this method)
cities16  = {"Tokyo", "Berlin","Delhi","Kanpur"}
cities16.add("Lucknow")
print(cities16)

#update (if you are add more than one item than you use this method)
    #We have seen above
#remove()/discard() (delete the item) 
#1- Remove(This will raise an Error)
#1- Discard(This will not raise an Error)
cities17  = {"Tokyo", "Berlin","Delhi","Kanpur"}
cities17.remove("Kanpur")
cities17.discard("Berlin")
print(cities17)

#pop()
""" This method remove the last item of the set but the catch is that we dont know that
    which item gets popped as sets are unordered.
    However you can access the popped item if you assign the pop() to variable
 """
cities18 ={"Nagpur", "Lucknow","Tokyo", "Berlin","Delhi","Kanpur"}
print("Original: ",cities18)
item = cities18.pop()
print(cities18)
print(item) # To view that which item is poped

#del(to delete whole set)
cities18 ={"Nagpur", "Lucknow","Tokyo", "Berlin","Delhi","Kanpur"}
#del cities18
print(cities18)

#clear(clear all item in set but not delete the whole set)
cities19 ={"Nagpur", "Lucknow","Tokyo", "Berlin","Delhi","Kanpur"}
cities19.clear()
print(cities19)