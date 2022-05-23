import random
from sys import platlibdir

rounds = 0
win1 = 0
win2 = 0
win_count = str(0)

def dice():
    dice_roll = random.randint(1,6)
    return dice_roll

n = int(input('enter the number of rounds to play :'))
player1 = input("enter name of first player : ")
player2 = input("enter name of second player : ")

for i in range(n):
    
    rounds += 1
    print("\n"," ROUND = ",rounds)
    
    p1 = dice()
    print(player1,"rolled = ",p1)
    p2 = dice()
    print(player2,"rolled = ",p2)
    
    if p1 == p2:
        print("DRAW!!!","\n")
    elif p1>p2:
        print(player1,"won by rolling ", p1)
        win1 += 1
        print(player1,"round won =",win1,"\n")
    else:
        print(player2,"won by rolling ",p2)
        win2 += 1
        print(player2,"round won =",win2,'\n')

for j in win_count:
    if win1 == win2:
        print("OOF  DRAW!!")
    elif win1>win2:
        print(player1,"wins by taking",win1, "rounds.","\n")
    else:
        print(player2,"wins by taking1",win2,"rounds.","\n")