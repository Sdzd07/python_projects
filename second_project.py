#this program give user id and email on our company
#add the name of company name in variable 
company_name = "HUNTER"
#company domain
company_domain = "@hunter.com"
#ask user for enter his&her name 
name = input("Enter your name: ").lower().title()
#ask user for birth year
birth_year = input("Enter your birth year: ")
#ask user to enter his&her email 
email = input("Enter your email: ")
#print underscore * 50
print("_"*50)
#change the input (name) to the list 
new_name = name.split()
#greeting the user on our company 
print(f"Hello {new_name[0]}!\nWelcome at Hunter Company")
##print underscore * 50
print("_"*50)
#id of user equal 3 first charactars of name company +"_"+ 2 last characters of the last name of user + birthyear  
employee_id = f"Your id is: {company_name[:3].lower()}-{name[-2:]}{birth_year}"
print(employee_id)
#new email equal the first part of user email + domaine name of the company 
email.rindex("@")
new_email = f"Your email is: {email[:5]}{company_domain} "
print(new_email)
print("_"*50)
