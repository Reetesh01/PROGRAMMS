import random
from traceback import print_tb

p1_r = 0
p2_r = 0
rounds = 0
round_win = str(1)
n = int(input("enter the nimber of rolls for the game = "))

def dice():
    dice_roll = random.randint(1,6)
    return dice_roll

player1 = input("enter name of player 1 = ")
player2 = input("enter name of player 2 = ")

for i in range(n):
    rounds = rounds+1
    print("----------> ROUND = ",rounds,"<----------","\n")
    p1 = dice()
    print(player1, "rolled = ",p1)
    p2 = dice()
    print(player2, "rolled = ",p2)
    
    if p1 == p2:
        print(player1,'and',player2,'rolled = ',p1, " and its a DRAW!!")
        
    elif p1>p2:
        p1_r += 1
        print(player1, "wins by rolling ", p1)
        print(player1,'round won = ',p1_r,"\n")
    else:
        p2_r += 1
        print(player2,"wins by rolling",p2)
        print(player2,'round won = ',p2_r,"\n")
        
    
for j in round_win:
    if p1_r == p2_r:
        print('DRAW')
    elif p1_r>p2_r:
        print(player1,"wins by ",p1_r," rounds!")
    else:
        print(player2 ,"wins by ",p2_r," rounds!")
