#program for guess Roll Dice 
#import random module 
import random 
roll_dice = random.randint(1,6)
gusse = int(input("Enter number between 1 to 6 :"))
print("-"*20)
print(f"The Roll Dice is {roll_dice}")
#check the answer of user
if gusse == roll_dice:
    print("You won!")
else: 
    print("You lost!")    
   
