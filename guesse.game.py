#program guessing number game program 
#always ask user to guess number between 1 and 100
#import module random
import random
number = 1
lst_number = []
random_lst = []
while number<=100: 
    lst_number.append(number)
    number+=1
while True:    
    print("_"*40)
    print("Enter number between 1 and 100")
    guess_number = input("guess the number:")
  
    random_number = random.choice(lst_number)
    random_lst.append(random_number)
    if len(random_lst)>=6 :
     print("You gessed the number in 5 attempts") 
     print("_"*40)
     break    
    elif guess_number.lower().strip()== "done" or len(guess_number)==0:
         print("Done!") 
         break    
    if 1<= int(guess_number)<=100: 
     if int(guess_number)<random_number:
         message = "Too loow, try again!"   
     elif int(guess_number)>random_number:
      message = "Too high, try again!" 
     else:    
           message = "Bravoo, you won!"     
    else:
        continue  
    print("_"*40)
    print(message)
