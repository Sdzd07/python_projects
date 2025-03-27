#Tell the user if the entered number is a prime number or not.
#get input from user 
number = int(input("Enter integer number: "))
#initialize variable to store factors
num_divisors = 0
#intialize for loop for 
for i in range(1,number+1):
# check if number is divisible by any number between 2 and itself    
    if number%i==0:
# increment the number of divisors        
        num_divisors+=1
#print result
if num_divisors==2:
    print(f" {number} is a prime number ")
else:
     print(f"{number} is not a prime number ")    
    
