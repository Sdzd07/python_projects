#Find the smallest, odd number in the following list without using min and sort. 
numbers = [-500, -694, -762, -445, -348, -361, -758, -594, 954, -861, -610, -549, -336, -400, -600, -836, -671, -573,555, -390, -450,
            -811, -849, -870, -815, -694, -951, -588, 484, -609, -674, -411, -408, -498, -649, -541, -441, -839, 567, -898
          ] 
#make list  for store on it the odd numbers 
lst_numbers =[]
#initialize for loop for numbers 
for num in numbers:
#check if num module to 2 equal 0     
    if num%2!=0:
#add odd num to the list       
        lst_numbers.append(num)
#make variable to store smaller number
smaller_num = lst_numbers[0]
#initialize for loop for lst_numbers
for num in lst_numbers:
#check if num is smallest    
    if num<smaller_num:        
        smaller_num = num 
#print result 
print(f"The smallest odd number is: {smaller_num} ")        