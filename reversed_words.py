#program for reversed words game
#import random module 
import random
#import time module
import time
#put a list of words
list_word = ['have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will', 'hope',
'there','make', 'when', 'more', 'other', 'what', 'time', 'about', 'than', 'into', 'could']
choice_word = random.choice(list_word)
#welcome to the game 
print("Welcome to the reversed words Game!")
print("_"*30)
#reversed the word 
reversed_word = choice_word[::-1]
print(f"The reversed word is: {reversed_word}")
print("_"*30)
#put variable for start time 
start_time = time.time()
#get input from user
guess = input("The word is: ")
print("_"*30)
#put variable for end time
end_time = time.time()
#calculate taken time
taken_time = int(end_time) - int(start_time)
#check_the inswer of user if correctly 
if  guess in list_word:
        if taken_time<=7:
                word ="You won!"
        elif taken_time>7:
                word = "You took too long time\nYou lost!"
else:        
    word = "Worng word!" 
print(word)      
