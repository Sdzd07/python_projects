#print the folwing info :
#Mohamed grades 
#Ali age 
#sara grades and age # each grade in line like this :
#100
#80
#90 
students = {
    "Ahmed":{
        "grades": [100,  90,  80], 
        "age": 20
        },
    "Ali":{
       "grades":[ 90, 100, 95],
        "age": 22
        },
    "Sara":{
        "grades":[80, 95, 100], 
        "age": 23
        }
}
#intilaiz for loop for print grades of ahmed 
ahmed_grades = students["Ahmed"]["grades"]
print(f"Ahmed grades is : ")
for grade in ahmed_grades :
    print(grade)
print("_"*40)
#print Ali age 
ali_age = students["Ali"]["age"]
print(f"Ali have {ali_age} years old")
print("_"*40)
#initilaiz for loop for print sara grades and age 
sara_grades = students["Sara"]["grades"]
print(f"Sara grades are : ")
for grade in sara_grades :
    print(grade)
#--------------------------------------------------
sara_age = students["Sara"]["age"]
print(f"Sara have {sara_age} years old ")
#--------------------------------------------------
#print the follwing information :
#Ahmed grades in math and english , and school
#Ali school , grades in history, scinece , arabic 
#sara grades in math , history, arabic 
students = {
    "Ahmed":{"grades":{
        "math":100, 
        "scinece": 90, 
        "english": 100, 
        "Arabic": 100
    },
        "school": "rahimi"
    },
    "Ali":{"grades":{
         "math":99, 
         "science": 100, 
         "history": 100, 
         "arabic": 100
    }, 
        "school": "rahimi"
    },
    "Sara": {"grades":{
        "math": 90, 
        "science": 100, 
        "history": 95, 
        "arabic": 98
    },
        "school": "kadri"
    }
}
#print ahmed grades in math , english and his school 
ahmed_grade_math = students["Ahmed"]["grades"]#["math"]# ahmed grade in math 
ahmed_grade_english = students["Ahmed"]["grades"]["english"]#ahmrd grad in english
ahmed_school = students["Ahmed"]["school"]# ahmed school
print(f"Ahmed get grade {ahmed_grade_math} in math")
print(f"Ahmed get grade {ahmed_grade_english} in english")
print(f"Ahmed school : {ahmed_school}")
print("_"*40)
#print ali school , grades in math , science, arabic 
ali_grade_math = students["Ali"]["grades"]["math"]#ali grade in math 
ali_grade_history = students["Ali"]["grades"]["history"]#ali grade in history
ali_grade_arabic = students["Ali"]["grades"]["arabic"]#ali grade in arabic 
ali_school = students["Ali"]["school"]#ali school
print(f"Ali grades: \nMath :{ali_grade_math} \nHistory : {ali_grade_history} \nArabic : {ali_grade_arabic}")
print(f"Ali school : {ali_school}")
print("_"*40)
#print sara grade in math, history, arabic 
sara_grade_math = students["Sara"]["grades"]["math"]#sara grade in math 
sara_grade_history = students["Sara"]["grades"]["history"]#sara grade in history
sara_grade_arabic = students["Sara"]["grades"]["arabic"]#sara grade in arabic 
print(f"Sara grades : \nMath : {sara_grade_math} \nHistory : {sara_grade_history} \nArabic : {sara_grade_arabic}")
print("_"*40)
#-----------------------------------------------------------------------
#print the follwing info:
#chicken burger price
#viggie pizza price 
#cocke price
#chocolate cacke price
##onine rings price
resturent_menu = {
    "Burgers":{
        "Beef": 80, 
        "Chicken": 70, 
        "Bacon": 90
     },
     "Pizzas": {
        "Cheese": 80, 
        "Pepperonie": 90, 
        "Veggie": 10
     },
     "Drinks": {
         "Coke": 40, 
         "Fanta": 50, 
         "Sprait": 30
                
     },
     "Desertes": {
         "Ice cream": 40, 
         "Chocolate Cake": 50
     },
     "Sides": {
         "Frias": 60, 
         "Onine Rings": 30, 
         "Potato Wedges": 20
     }
}
#print chicken burger
print("Chiken burger price is :", resturent_menu["Burgers"]["Chicken"] )
#print veggie price 
print("Veggie pizza price is :", resturent_menu["Pizzas"]["Veggie"])
#print cocke drinks price
print("Cocke drink price : ", resturent_menu["Drinks"]["Coke"])
#print chocolate cacke price 
print("Chocolate cake price :", resturent_menu["Desertes"]["Chocolate Cake"])
#print onine rings price 
print("Onine rings price is :", resturent_menu["Sides"]["Onine Rings"])
print("_"*40)
#print the follwing information:
#Mohamed karim , Rami Ahmed (age , salary, department) 
#Reda ghani department 
#All the information about Mohamed karim and Rami Ahmed in the follwing format:
#Mohamed karim is 23 years old, he work in HD department and his salary is 12.000 $
employees = {
    "Mohamed Karim": {
        "Age": 23,  
        "Salary": 10.000, 
        "Department": "IT"
    },
    "Reda Ghani": {
        "Age": 25, 
        "Salary": 9000, 
        "Department": "HR"
    },
    "Rami Ahmed": {
        "Age": 22,
       "Salary": 11.000, 
       "Department": "IT"
    }
} 
#print Mohamed karim , Rami Ahmed (age , salary, department) 
ahmed_karim_age = employees["Mohamed Karim"]["Age"]
ahmed_karim_salary = employees["Mohamed Karim"]["Salary"]
ahmed_karim_department = employees["Mohamed Karim"]["Department"]
print(f"Mohamed Karim is {ahmed_karim_age} years old, he work in {ahmed_karim_department} department and his salary is {ahmed_karim_salary:.3f} ")
print("_"*40)
rami_ahmed_age = employees["Rami Ahmed"]["Age"]
rami_ahmed_salary = employees["Rami Ahmed"]["Salary"]
rami_ahmed_department = employees["Rami Ahmed"]["Department"]
print(f"Rami Ahmed is {rami_ahmed_age} years old, he work in {rami_ahmed_department} department and his salary is {rami_ahmed_salary:.3f} ")
print("_"*40)
#print Reda Ghani department 
print("Reda Ghani department is :",employees["Rami Ahmed"]["Department"])
print("_"*40)
#Print the total percentage of Ali score using the following information.
students = {
    "Mohamed": {"grades": {
        "math": 100,
        "english": 90,
        "science": 80,
        "arabic": 100,
        "history": 97
    },
        "school": "Codezilla"
    },
    "Ahmed": {"grades": {
        "math": 100,
        "english": 95,
        "science": 93,
        "arabic": 100,
        "history": 94
    },
        "school": "Codezilla"
    },
    "Ali": {"grades": {
        "math": 85,
        "english": 83,
        "science": 87,
        "arabic": 100,
        "history": 90
    },
        "school": "Al-Azhar"
    }
}
mohamed_grades = students["Mohamed"]["grades"]
grades_list = []
for grade in mohamed_grades:
    grades_list.append(mohamed_grades[grade])
overage_grades = sum(grades_list)/len(grades_list)
print(f"The overage prcentage grades of Mohamed is : {overage_grades:.2f} %")
print("_"*40)
#without use sum and lenght functions :
mohamed_grades = students["Mohamed"]["grades"]
index = 0
sum_grades = 0
for grade in mohamed_grades:
    sum_grades+= mohamed_grades[grade]
    grades_list.append(mohamed_grades[grade])
    index +=1
overage_grades = sum_grades/index
print(f"The overage prcentage grades of Mohamed is : {overage_grades:.2f} %")
print("_"*40)
#-------------------------------------------------------------------
ahmed_grades = students["Ahmed"]["grades"]
grades_list = []
for grade in ahmed_grades:
    grades_list.append(ahmed_grades[grade])
overage_grades = sum(grades_list)/len(grades_list)
print(f"The overage prcentage grades of Ahmed is : {overage_grades:.2f} %")
print("_"*40)
#without use sum and lenght functions :
ahmed_grades = students["Ahmed"]["grades"]
index = 0
sum_grades = 0
for grade in ahmed_grades:
    sum_grades+= ahmed_grades[grade]
    grades_list.append(ahmed_grades[grade])
    index +=1
overage_grades = sum_grades/index
print(f"The overage percentage grades of Ahmed is : {overage_grades:.2f} %")
print("_"*40)
#---------------------------------------------------------------------
ali_grades = students["Ali"]["grades"]
grades_list = []
for grade in mohamed_grades:
    grades_list.append(ali_grades[grade])
overage_grades = sum(grades_list)/len(grades_list)
print(f"The overage prcentage grades of Ali is : {overage_grades:.2f} %")
print("_"*40)
#without use sum and lenght functions :
mohamed_grades = students["Ali"]["grades"]
index = 0
sum_grades = 0
for grade in ali_grades:
    sum_grades+= mohamed_grades[grade]
    grades_list.append(ali_grades[grade])
    index +=1
overage_grades = sum_grades/index
print(f"The overage percentage grades of Mohamed is : {overage_grades:.2f} %")
print("_"*40)




        

