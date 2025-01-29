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
    #analyse the minimum salary in the list by using max method 
     min_salary = min(float_salaries)
    #for know the average salary should do  total of the salaries / number of salaries 
     sum_salaries = sum(float_salaries)
     average_salary = sum_salarys/len(float_salaries)
    #result 
     print(f"The maximum salary is: {max_salary} $")     
     print(f"The minimum salary is: {min_salary} $")   
     print(f"The average salary is: {average_salary} $")
