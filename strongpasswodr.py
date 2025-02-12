# program generate strong password containing letters, numbers, and punctuations
#import string module 
import string 
#import random module
import random 
#greate variable for store on it the characters  
password = ""
#get the desired password length 
length_character = int(input("Enter the desired password length: "))
# Loop until the password string has the desired length
while len(password)< length_character:
     # Add a random character from a set of letters, digits, and punctuation
     characters = string.ascii_letters + string.digits + string.punctuation
     choice_character = random.choice(characters)
     password += choice_character
#print the generated password 
print(f"The generated password is: {password}")