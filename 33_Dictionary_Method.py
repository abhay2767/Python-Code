#update(Here you can take all keys with value of another dictionary to previous dictionary)
emp_id = {122: 45, 123:89, 124:59, 125:68,126:98}
emp_id1 ={222:67, 566:95}
emp_id.update(emp_id1)
print(emp_id)

#clear(This will clear all keys and value of dictionary and leave Empty Dictionary)
print("Before clear(): ",emp_id1)
#emp_id1.clear()
print("After clear(): ",emp_id1)

#pop(This will pop or remove the given key value pair)
print("Before pop(): ",emp_id)
emp_id.pop(122)
print("After pop(): ",emp_id)
emp_id.popitem() #By deafult this will remove last key value pair
print("After popitem(): ",emp_id)

#del(This will delete the whole given dictionary)
print("This is Before emp_id1(): ",emp_id1)
#del emp_id1
del emp_id1[566]
print("This is After emp_id1(): ",emp_id1) #This will raise an Error because emp_id1 was deleted