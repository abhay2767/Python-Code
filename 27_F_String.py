#String formatting earlir not convinient
""" text  = "Hey my name is {1} and i am from {0}"
name = "Abhay"
State = "Utter Pradesh"

print(text.format(State,name)) """

#String formatting Now convinient
text  = "Hey my name is {1} and i am from {0}"
name = "Abhay"
state = "Utter Pradesh"
print(text.format(state, name))
print(f"Hey my name is {name} and I am from {state}")

price = 49.251436
txt = f"For only {price:.2f}" #2 decimal point
print(txt)
#or
print(txt.format())