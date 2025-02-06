#program for guess the secret number
#import random module 
import random 
secret_number1 = random.randint(1,20)
secret_number2 = random.randint(1,20)
secret_number3 = random.randint(1,20)
secret_number4 = random.randint(1,20)
#put list for winners numbers
won_numbers = [secret_number1, secret_number2, secret_number3, secret_number4]
#get input from user
guess = int(input("Enter number between 1 to 20 :"))
#check the input if is correctly & print result
if 1>guess or guess>20:
    input("Please enter number between 1 to 20: ")
elif guess in won_numbers:
    print("Bravooo you won!")
else: 
    print("Sorry you lost!" )    
  
     

