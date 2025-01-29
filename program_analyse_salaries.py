#this script analyse the salary on the list and give the user the Maximum&Minimum and the Average of salary
#first step ask user for input all the salaries,or we can put early list.
salaries = input("Enter more than one salary and separeat between salaries by comma please : ")
comma = ","
if  comma not in salaries or salaries == comma:
    print("Please enter more than one salary and use comma to separeat between the salaries ")
else:
    #change the input form to the list by using split method 
     list_salariess = salaries.split(",")
    #first should be change the items on the list from string data type to float data types by using map method 
    # or with while (for loops)
     float_salaries = list(map(float,list_salariess))
    #analyse the maximum salary in the list by using max method 
     max_salary = max(float_salaries)
     print(f"The maximum salary is: {max_salary} $")
    #analyse the minimum salary in the list by using max method 
     min_salary = min(float_salaries)
     print(f"The minimum salary is: {min_salary} $")
    #for know the medium salary from the list we should addition all the items on the list together
    # and division the total on number of items have on the list (salaries)
     sum_salarys = sum(float_salaries)
     average_salary = sum_salarys/len(float_salaries)
     print(f"The average salary is: {medium_salary} $")
