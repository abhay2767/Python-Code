#You can use else with for loop and while loop also.
for i in []:
    print()
else:
    print("sorry no i")

#Quiz tell me the ouput that what hapeen this will go inside else or not: 
# No, Here if loop was succesfuly finish not Break  because loop go thought this last value
for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("sorry no i")
print("Out of loop")
      
print("same with while loop")
i =0
while i< 7:
    print(i)
    i = i+1
    if i == 4:
        break
else:
    print("sorry no i")
print("Out of loop")