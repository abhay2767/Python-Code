a = True
#print(a=False) #We can not do this in python
print(a:=False) #Now using Walrus operator we can assign the value to the varibale in conditions and loops and within expression

numbers = [1,2,3,4,5]

while(n:= len(numbers)>0):
    print(numbers.pop())
    print(numbers)
#this is now empty

happy = True
print(happy)
print(happy := False)

#Without Walrus operator
food = list()
while True:
    food = input("What food do you like: ")
    if food == "quit":
        break
    food.append(food)

#With Walrus operator
    while(food := input("What food do you like: ")) != "quit":
        food.append(food)

