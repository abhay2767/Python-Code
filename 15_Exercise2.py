import time
#timestamp = time.strftime('%H:%M:%S')
#print(timestamp)
hour = int(time.strftime('%H'))
hour = int(input("Enter time in hour "))
#print(hour)

if(hour>=0 and hour<12):
    print("Good Morning")
elif(hour>=12 and hour<17):
    print("Good Afternoon")
elif(hour>=17 and hour<=23):
    print("Good Night")
    