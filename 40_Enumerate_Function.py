#Print anything using to index
#First way
marks = [12, 56, 89, 59, 75, 65,39,19]
index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("Good")
    index +=1 

#Secand way 
for index, mark in enumerate(marks, start=1): #Here start = 1 mean index will start from 1
    print(mark)
    if(index == 3):
        print("Good marks")