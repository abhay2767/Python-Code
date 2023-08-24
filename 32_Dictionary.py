#Basically you can create mapping using dictionary and Dictionary are oredered after 3.7 version
dic ={
    "Name": "Abhay",
    "Age": 23,
    "Address": "Kanpur"
}
print(dic)
print(dic["Name"])

dic1 = {
    21689 : "PSIT",
    22612 : "WCTM"
}
print(dic1[21689])

info ={"Name": "Rohan", 'age': 23, 'eligible': True}
print(info)
print(info["Name"])
print(info["age"])
print(info.get('eligible'))

#print(info["eligible1"]) # This will show you an Error when item in not availble
print(info.get('eligible1')) # Not Show any Error just show 'None'

#Accessing all key of item
print(info.keys())
#Accessing all key's Value
print(info.values())
#using for loop accesing key's value
for key in info.keys():
    #print(info[key])
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items()) #key value pairs
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")