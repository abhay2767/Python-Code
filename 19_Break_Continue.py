#Break
for i in range(11):
    if( i == 5):
        print("Out from loop")
        break
    print("5 X", i+1, "=", 5 * (i+1))
print("Loop out")

#Continue
for  i in range(15):
    if( i == 10):
        print("Skip the iteration")
        continue
    print("5 X", i+1, "=", 5 * (i+1))
print("Loop out")