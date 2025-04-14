#Make a List with 20 random numbers between 100 and 1000. 
#import random module 
import random 
random_list = [random.randint(100,1000) for _ in  range(20) ]
#print the list with 20 random numbers 
print(random_list)
