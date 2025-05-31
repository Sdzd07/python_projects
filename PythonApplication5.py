#Print the following menu in a nice format for the user.
pizzas = {"Margherita": 100,
"Pepperoni": 120,
"Meat Lovers": 150,
"Chicken": 130,
"Chicken Ranch": 140,
"Cheese": 110
}
#initialize for loop to print each item and price 
for pizza in pizzas:
    print(f"{pizza} pizza, price : {pizzas[pizza]}")
print("_"*40)
#other way
for pizza, price in pizzas.items():
    print(f"{pizza} pizza, price : {price}")
print("_"*40)
#Using the following information make a program that allows the user to get the school of the student
#when they enter the student name or the student id.
schools = {
"Codezilla School":
{'1100':"Mohamed Gouda", '1101':"Islam Hesham",
'1102':"Ayman Mohamed", '1103':"Ahmed Khaled"},
"Al Dorra School":
{'2100':"Ahmed Hassan", '2101':"Mahmoud Ali",
'2102':"Adham Wael", '2103':"Khaled Ali"},
"Mostafa Kamel School":
{'3105':"Hazem Ahmed", '3106':"Omar Mohamed",
'3107':"Hussein Kamal", '3109':"Ali Ahmed"}
}
#get input from user 
user_input = input("Enter the student name or  the id to search for : " ).lower().title()
# flag to check if the user input is found or not
not_found = True
# loop over the schools
for school in schools:
    for students_ids,student_name in schools[school].items():     
# check if the user input is in the students ids or names
        if (user_input in schools[school]) or (user_input in schools[school][students_ids]):
            print(f"{user_input} is student on {school}")
            not_found = False
            break
# if the user input is not found
if not_found:
    print(f" {user_input} is not in our records")
print("_"*40)
#other solution 
# get user input
user_input = input("Enter student name or id to search for:").lower().title()
# flag to check if the user input is found or not
not_found = True
# loop over the schools
for school in schools:
# get the students ids and names
    students_ids = schools[school].keys()
    students_names = schools[school].values()
# check if the user input is in the students ids or names
    if (user_input in students_ids) or (user_input in students_names):
        print(f"{user_input} is a student in {school}")
        not_found = False
        break
# if the user input is not found
if not_found:
    print(f"{user_input} is not in our records")
print("_"*40)
#------------------------------------------------
#Increase the salaries of the following employees by 40%.
employees = {
"Ahmed Hassan": 12_000,
"Mohamed Ahmed": 20_000,
"Ali Ahmed": 15_000,
"Khaled Ali": 10_000,
"Omar Mohamed": 13_000,
"Hazem Ahmed": 24_000,
}
for employee, salary in employees.items():  
    employees[employee] = (salary*1.4)
    print(f"{employee} salary : {salary:.2f}")
#other solution 
employees_ = {
"Ahmed Hassan": 12_000,
"Mohamed Ahmed": 20_000,
"Ali Ahmed": 15_000,
"Khaled Ali": 10_000,
"Omar Mohamed": 13_000,
"Hazem Ahmed": 24_000,
}
for employee in employees_:  
    price = employees_[employee]
    employees_[employee] = price+(price*0.4)
    print(f"{employee} salary : {price:.2f}")