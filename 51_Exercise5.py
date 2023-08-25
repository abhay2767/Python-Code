#Snake water Gun:-
""" 
    1:-Snake water and gun is a variation of the children's game "rock-paper-scissors" 
    where playes use hand gestures to represent a snake, water, or a gun. The gun beats the
    snake the gun, and the snake beats the water.
    2:-Write a pyhton program to create a Snake Water Gun Game in python using if-else statement
    Do not create any fancy GUI. use proper functions to check for win
               S W G
Computer =      0_1_2
Player   = S 0 |D W L
           W 1 |L D W
           G 2 |W L D

S, W, G = Snake, Water, Gun
D, W, L = Draw, Win, Lose
 """



import random
def check(comp, user):
    if comp == user:
        return 0
        if(comp == 0 and user == 1):
            return -1
        if(comp == 1 and user == 2):
            return -1
        if(comp == 2 and user == 0):
            return -1
    return 1
    
    
comp = random.randint(0,2)
user = int(input("O for Snake, 1 for Water and 2 for Gun: "))

score = check(comp,user)
print("You: ",user)
print("Comp: ",comp)
if(score == 0):
    print("Its a draw")
elif(score == 1):
    print("you lose")
else:
    print("You win")