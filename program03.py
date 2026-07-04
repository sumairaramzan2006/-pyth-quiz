import random
def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print(f"you rolled: {dice1} + {dice2} =  {total}")
    return total
input("enter first roll...")
first_roll = roll_dice()
if first_roll == 7 or first_roll == 11:
    print("congratualtion: you win")
elif  first_roll == 2 or first_roll == 3 or first_roll == 12:
    print("you loss")
else:
    point = first_roll
    print("your point is:", point)
    for i in range(3):
        
        input("enter a roll")
        new_roll = roll_dice
        if new_roll == point:
            print("you win")
            
        else:
            print("you loss")
print("\n========GAMAE OVER=========")
        
   
    
    