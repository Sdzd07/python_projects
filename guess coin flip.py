#import random module 
import random 
#get guess from the user
guess = int(input("Guess the coin flip!\n1- For a Heads\n2- For Tails\nChoice 1 or 2 : "))
#random coin flip
choice = random.randint(1,2)
#coin flip
if choice == 1:
    coin = "The coin is Heads"
else:
    coin = "The coin is Tails"
#check if the user guessed correctley and print the result
if guess == choice:
    result = "You won!"
else:
    result = "You lost!"
print("_"*40)
print(f"{coin}\n{result}")
print(choice)