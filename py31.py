#Make list with 100 random numbers between 100 and 10,000 that are divisible by 3 and 5. 
#improt random module 
import random 
list_numbers = [random.randint(100,10_000)  for num in range(100,100_000)if num%3==0 and num%5==0 ]
print(list_numbers)
random_list_numbers = [ random.choice(list_numbers) for _ in range(100) ]
print(random_list_numbers)