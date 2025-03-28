#Make your own Multiplication table like the following. 
index = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#initialize while loop
while index<len(numbers):
#initialize for loop     
    for i in range(1,len(numbers)+1):#  for i in numbers:
        calculate = i*numbers[index]
#print result         
        print(f"{numbers[index]} x {i} = {calculate}")  
    index+=1
    print("-"*20)
#######################################################
for i in range(1,11):
    for e in range(1,11):
        calculate = i * e 
        print(f"{i} x {e} = {calculate}")
print("-"*20)            

    



    

    





           
