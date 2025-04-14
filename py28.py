#Make the following numbers negative. 
nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]
nigative_num = [- num for num in nums]
print(nigative_num)
#second way 
nigative_n = []
for num in nums:
    nigative_n.append(-num)
print(nigative_n)    
#another exe:
#Create a new list with the square of the numbers in the given list. 
nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27] 
square_number = [num**2 for num in nums]
print(square_number)
square_nums = []
for i in range(len(nums)):
    square_nums.append(nums[i]**2)           
print(square_nums)    
#exe 3
#create a new list with the scores as percent and each score in the format of 88% 
scores = [75, 87, 93, 98, 82, 67, 91, 88] 
new_list = [str(score) + "%" for score in scores]
print(new_list)
######################################
#exe 4
#Make a list with all the items in the following list in lowercase. . 
fruits = ["APPLE", "ORANGE", "BANANA", "PEAR", "MANGO"] 
fruitss = [fruit.lower() for fruit in fruits ]
print(fruitss)
####################################
#exe 5
#Write code to find the sum of the even numbers in the list. 
nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]
sum_even_numbers =sum([num for num in nums if num%2==0])
print(sum_even_numbers)
###################################
#exe 6
#Make a new list with prices in the following form $10.99. 
prices = [10.99, 20.99, 30.99, 40.99, 50.99] 
list_prices = ["$"+ str(price) for price in prices]
print(list_prices)