#Flat a nested list in 2 Ways. . 1 
# nested_list = [["Hello", "from", "Codezilla"],  ["Python", "Course", "is", "awesome"],  ["I", "enjoy", "learning", "Python", "with", "Codezilla"]]    
# intilais nested list
nested_list = [["Hello", "from", "Codezilla"],  ["Python", "Course", "is", "awesome"],  ["I", "enjoy", "learning", "Python", "with", "Codezilla"]]
#make variable to store all values in on list not in nested
lst_1 = []
#intilia for loop  for ech list
for lst in nested_list:
#intilias for loop for each word    
    for word in lst:
        lst_1.append(word)
#print list
print(lst_1)
###############################################
#way 2
# nested_list = [["Hello", "from", "Codezilla"],  ["Python", "Course", "is", "awesome"],  ["I", "enjoy", "learning", "Python", "with", "Codezilla"]]    
# initialize nested list
nested_list = [["Hello", "from", "Codezilla"],  ["Python", "Course", "is", "awesome"],  ["I", "enjoy", "learning", "Python", "with", "Codezilla"]]
#make variable to store all values in on list not in nested
list_2 = []
#initialize for loop  for ech list
for lst in nested_list:
#initialize for loop for each word    
    for word in lst:
        lst_1.append(word)
#print list
print(lst_1)
#############################################
#Find the smallest multiple of 9 in the following list
#initialize variable for store the multiple number of 9 
numbers_list = [511, 260, 261, 912, 362, 473, 893, 277, 351, 494, 486, 885, 341, 484, 598, 950, 859, 716, 488, 584] 
#initialize variable for store the multiple number of 9 
numbers_list.sort()
numbers = 0
#initialize for loop 
for num in numbers_list:
#see if i is multiple of 9 or no    
    if num%9==0:
#add the i in the list           
#use sort the list descending for 
#print the smaller multiple number of 9 
        
     print(f"The smaller multiple number of 9 is: {num}")
     break
###############################################
#way 2
#initialize variable for store the multiple number of 9 
numbers_list = [511, 260, 261, 912, 362, 473, 893, 277, 351, 494, 486, 885, 341, 484, 598, 950, 859, 716, 488, 584] 
#initialize variable for store the multiple number of 9 
numbers = []
#initialize for loop 
for i in numbers_list:
#see if i is multiple of 9 or no    
    if i%9==0:
#add the i in the list        
        numbers.append(i)   
#find the smaller number in the list 
min_number = min(numbers) 
#print the smaller multiple number of 9 
print(f"The smaller multiple number of 9 is: {min_number}")
###########################################
numbers = [-588, -479, -713, -701, -885, -578, -835, -466, -935, -665, -360, -837, -389, -367, -454, -668, -907, -822, -541, -680, -405, -330, -625, -916, -331, -876, -689, -753, -810, -648, -787, -952, -718, -401, -502, -699, -533, -450, -580, -725]  
# initialize the largest number 
largest = numbers[0]  
# # loop through the list 
for number in numbers:     
# # check if the number is larger than the largest number     
    if number > largest:        
# update the largest number         
        largest = number  
print(f"The largest number is {largest}") 