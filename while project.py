#program print the total number from 0 to 100
total_number = 0
number = 0
while number<=100:
    print(number)
    total_number +=number
    number +=1
    print(total_number)
#program print the total of numbers between 70 to 160  
print("_"*50)
total_number = 0
number = 70 
while number<= 160:
    print(number)
    total_number += number
    number +=1
print(total_number)
# program print the total of even numbers between 30 to 470
print("_"*50)
sum_even_number = 0
number = 30   
while number<=470:
    print(number)
    sum_even_number +=number    
    print(sum_even_number)
    number +=2
#program Print the total of numbers that are divisible by 3 and between 1 to 1000. 
print("_"*50)
number = 1
while number<1000:
    if number%3 == 0:
        print(number)
    number += 1
       
