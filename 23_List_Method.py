l = [11,59,1,1,1,1,9,8,2,3,6]
print(l)
print(l.index(3)) #This eturn the index of the first occurence of the list item
l.append(7) #Add item in list
print(l)
l.sort(reverse=True) #Sort the list Decrement
print(l)
l.sort(reverse=False) #Sort the list Increment
print(l)
print(l.count(1)) #How many time 1 is present in list

#copy
m = l #b create copy of the list
m[0] = 0 # This will change the value at given index in original list
print(l)

m = l.copy()
m[0] = 0 
print(m)

#Insert at given index
m.insert(1,899)
print(m)

#extend (merge the list to other list at last) 
new_list = [100,101,103]
l.extend(new_list)
print(l)
 
#doing concat with other way
k = m+new_list
print(k)