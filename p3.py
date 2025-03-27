# 1. print a list of odd numbers from 1 to 100
numbers = range(1,100,2)
print(list(numbers))
#######################################################
# 2. print a list of even numbers from 8 to 422
even_numbers = list(range(8,422,2))
print(even_numbers)
#######################################################
# 3. print a list of numbers from 120 to 450, increasing by 7
numbers = list(range(120,450,7))
print(numbers)
#######################################################
# 4. print the sum of even numbers from 28 to 228
even_num = range(28,229,2)
sum_even_num = 0
for num in even_num:
    sum_even_num+=num
print(sum_even_num)    
#############################################
even_num = list(range(28,229,2))
sum_even_num = sum(even_num)
print(sum_even_num) 
############################################
# Print the total of numbers between 0 to 100. 
total = 0
for i in range(101):    
    total+=1
print(i) 
############################################
# Print the total of numbers between 70 to 160. 
total = 0
for i in range(70,161):
    total+=i
print(i) 
############################################
# Print the total of even numbers between 30 to 470. 
total= 0
for i in range(30,471,2):
    total+=i
print(i)             
###########################################
#Print the total of numbers that are divisible by 3 and between 1 to 1000. 
total = 0
for i in range(3,1000,3):
    total +=i
print(i)
#Make a program that calculate the average of the second highest and second lowest numbers that are between 452 and 983 and are divisible by 5 and 7. 
list_num = []
for i in range(452,984):
    if (i % 5== 0) and (i %7 == 0):
        list_num.append(i)
hight_second_num = list_num[-2]   
low_second_num = list_num[1]
average = (hight_second_num + low_second_num) /2
print(f"The average of hightes second {hight_second_num} number and the lowest second {low_second_num} number is {average}")
