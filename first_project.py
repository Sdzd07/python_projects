#ask user to enter his&her full name 
full_name = input("Enter your full name please: ").lower().title()
# change input(full_name) to the list 
name_lst = full_name.split()
# greeting the user by his&her first name on our company and store it on variable (message)
message = f'Hello, {name_lst[0]}!\nWellcome at Saliho Company!'
#print the variable (message) 
print("_"*50)
print(message)
print("_"*50)