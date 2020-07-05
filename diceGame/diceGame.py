import random as rand
class Dice:
    def __init__(self, side_num=6):
        self.side_num=side_num
        self.face=0
        self.roll()
    def roll(self):
        self.face=rand.randint(1,self.side_num)
    def show(self):
        return self.face

class Player:
    def __init__(self,name):
        self.name=name
        self.points=0
        self.mydice=[]
        [self.mydice.append(Dice())for i in range(5)] 

    def roll(self):
        # roll all 5 dice
        [self.mydice[i].roll()for i in range (5)]
        # Show initial result
        print("Your initial roll is: ")
        drawResult(self.mydice)

    def re_roll(self,reRolls):
        for reRoll in reRolls.split():
            index=int(reRoll.rstrip())
            self.mydice[index-1].roll()
        drawResult(self.mydice)

def dice2Str(num):
    if num==1:
        d06="  _____________  "
        d00=" /___________ /| "
        d01="|            | | "
        d02="|            | | "
        d03="|      *     | | "
        d04="|            | | "
        d05="|____________|/  "
        d=[d06,d00,d01,d02,d03,d04,d05]
        return d 
    elif num==2:
        d06="  _____________  "
        d00=" /___________ /| "
        d01="|            | | "
        d02="|            | | "
        d03="|   *    *   | | "
        d04="|            | | "
        d05="|____________|/  "
        d=[d06,d00,d01,d02,d03,d04,d05]
        return d
    elif num==3:
        d06="  _____________  "
        d00=" /____________/| "
        d01="|            | | "
        d02="|         *  | | "
        d03="|      *     | | "
        d04="|   *        | | "
        d05="|____________|/  "
        d=[d06,d00,d01,d02,d03,d04,d05]
        return d 
    elif num==4:
        d06="  _____________  "
        d00=" /____________/| "
        d01="|            | | "
        d02="|   *     *  | | "
        d03="|            | | "
        d04="|   *     *  | | "
        d05="|____________|/  "
        d=[d06,d00,d01,d02,d03,d04,d05]
        return d 
    elif num==5:
        d06="  _____________  "
        d00=" /____________/| "
        d01="|            | | "
        d02="|   *     *  | | "
        d03="|      *     | | "
        d04="|   *     *  | | "
        d05="|____________|/  "
        d=[d06,d00,d01,d02,d03,d04,d05]
        return d 
    elif num==6:
        d06="  _____________  "
        d00=" /____________/| "
        d01="|            | | "
        d02="|   *     *  | | "
        d03="|   *     *  | | "
        d04="|   *     *  | | "
        d05="|____________|/  "
        d=[d06,d00,d01,d02,d03,d04,d05]
        return d 
    else:
        d06="  _____________  "
        d00=" /____________/| "
        d01="|            | | "
        d02="|            | | "
        d03="|      ?     | | "
        d04="|            | | "
        d05="|____________|/  " 
        d=[d06,d00,d01,d02,d03,d04,d05]
        return d 

def drawResult(my_dice):
    # Dices is a list of Dice objects
    d=[]
    for dice in my_dice:
        d.append(dice2Str(dice.show()))
    print(d[0][0]+d[1][0]+d[2][0]+d[3][0]+d[4][0])
    print(d[0][1]+d[1][1]+d[2][1]+d[3][1]+d[4][1])
    print(d[0][2]+d[1][2]+d[2][2]+d[3][2]+d[4][2])
    print(d[0][3]+d[1][3]+d[2][3]+d[3][3]+d[4][3])
    print(d[0][4]+d[1][4]+d[2][4]+d[3][4]+d[4][4])
    print(d[0][5]+d[1][5]+d[2][5]+d[3][5]+d[4][5])
    print(d[0][6]+d[1][6]+d[2][6]+d[3][6]+d[4][6])
    [print(f"       {my_dice[i].face}         ",end='') for i in range(5)]
    print("\n      [1]              [2]              [3]              [4]              [5]            ")
   
# Initialize 5 dice
print("===================")
print("Welcome to Yahtzee!") 
print("===================")
#Initialize players
p1=Player(input("Player one enter your name: ").title())
p2=Player(input("Player two enter your name: ").title())

#Initial Roll Phase
print(f"{p1.name}, rolls! ")
p1.roll()
# Re-Roll Phase
for i in range(2):
    again=input("do you wish to reRoll?(y/n): ")
    if again.lower()=="n":
        break
    else:
        reRolls=input("which dice do you want to re roll?\n (enter list separated by spaces):")
        p1.re_roll(reRolls)

ready=input(f"{p2.name} are you ready to roll?(y/n): ")
#Initial Roll
print(f"{p2.name}, rolls! ")
p2.roll()
# Re-Roll Phase
for i in range(2):
    again=input("do you wish to reRoll?(y/n): ")
    if again.lower()=="n":
        break
    else:
        reRolls=input("which dice do you want to re roll?\n (enter list separated by spaces):")
        p2.re_roll(reRolls)




