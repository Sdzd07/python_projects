#program for calculate the age of user let's start:
#first we need to get input from user 
full_name = input("Enter your full name: ").strip().title()
birth_date = input("Enter your birth date (dd_mm_yyyy): ")
current_year = int(input("Enter the current year: "))
# second output message for greeting user by only the first name, so for do that we can use tow solution
#we can use split method or index method
#the problme is how we can output the first name only without last name of user 
#first solution we can do that y using index method will use it for know where is the index of space on the input 
name_index = full_name.index(" ")
#after know the index of space now will do this step
#output message of user 
print("_"*50)
print(f"Hello, {full_name[0:name_index]}!\nWellcom at Age calculator ")
#now we need to do operater for give age of user
# for do that we need to subtract the birth year of user from current year 
#but the problem is how we can silce only the brith year without the date and month 
#solution is 
birth_year = int(birth_date[-4:])
age = current_year-birth_year
print("_"*50)
print(f"Your age is : {age} ")

