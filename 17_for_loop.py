name = "Abhay Dubey"
for i in name:
    print(i)
    if(i == " "):
        print("White Space")

color = ["Red", "Blue", "Green"]
for colors in color:
    print(colors)
    for i in colors: #iterate list
        print(i)

#Range
for k in range(5): # By default start from zero
    print(k+1)

for k in range(1,10): #This will print 1 to 9 because it goes like 0 to n-1
    print(k)

for k in range(1, 10, 2): #(start, end, skip)
    print(k)