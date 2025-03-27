#great a new list with suqare nubmber in the given list 
numbers = [1, 2, 3, 4, 5] 
list_number =[]
for num in numbers:
    square_number  = num**2
    list_number.append(square_number) 
print(f"The square number for this list of number: {numbers} is {list_number}")    
print("_"*50)
#create a new list with the scores as percent and each score in the format of '88% ' 
scores = [75, 87, 93, 98, 82, 67, 91, 88]
list_scores =[]
for num in scores:
    score = str(num) + "%"
    list_scores.append(score)
print(list_scores)    
print("_"*50)
#Make a list with all the items in the following list in lowercase. 
fruits = ["APPLE", "ORANGE", "BANANA", "PEAR", "MANGO"] 
lower_list = []
for frt in fruits:
    lower_list.append(frt.lower())
print(lower_list)
print("_"*50)
#Make a list with all the items in the following list in title case. 
names = ["mohamed gouda", "reda ahmed", "ayman salim", "hassan ali", "nasro amine"] 
titl_case = []
for name in names:
    titl_case.append(name.title())
print(titl_case)    
#Make a list from the letters of the user string in uppercase. 
list_charcters = []
message = input("Enter string: ")
for char in message:
        list_charcters.append(char.upper())
print(list_charcters)            