tommato = 70;
budget = int(input("Enter your budget "))
if(budget - tommato >= 30):
    print("You can purchase Potato")
elif(budget - tommato >= 20):
    print("You can purchase carret")
elif(budget - tommato >= 10):
    print("You can purchase Chilly")
else:
    print("Sorry! Not have enought money to buy Potato or Carret")
print("Have a good day")