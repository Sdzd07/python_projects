#make program intrect with user like the folwing 
#pleas enter the name of student, mohamed hassen 
#Mohamed hassen got the follwing grades:
#Math: 100
#Arabic: 100
#Sience: 90
#History: 88
#English: 80
#----------------------------------------------
#Mohamed Hassen percentage's is %
#----------------------------------------------
#pleas enter the name of student: aymen 
#sorry we dont have info about aymen
students = {
    "Mohamed Hassen": {
        "Grades": {
            "Maht": 100, 
            "Arabic": 100, 
            "Sinece": 90,
            "History": 88, 
            "English": 80
            },
        "School": "Rahimi"
        },
    "Ahmed Karim":{
        "Grades":{
            "Math": 89, 
            "Arabic": 96, 
            "Sience": 100, 
            "History": 99, 
            "English": 100
            }, 
        "School": "Rahimi"
        }   
   }

#initialize while loop 
while True:
    input_user = input("Please enter the name of student you search for or (prees enter to quit program): ").lower().title()
    if len(input_user)==0:
        break
    if input_user in students:
        student_grades = students[input_user]["Grades"]
        total_grades = 0
        lenght_grades = 0
        print(f"{input_user} got the follwing grades: ")
        for grade in student_grades:
            total_grades+= student_grades[grade] 
            lenght_grades+=1
            print(f"{grade}: {student_grades[grade]} ")
        overage_grades = total_grades/lenght_grades
        print("_"*60)
        print(f"{input_user} percentage's is {overage_grades:.2f}%")
    else:
        print(f"Sorry we dont have information about {input_user}")
#######################################################################
    print("_"*60)
#other solition 
#initialize while loop 
while True:
    input_user = input("Please enter the name of student you search for or (prees enter to quit program): ").lower().title()
    if len(input_user)==0:
        break
    if input_user in students:
        student_grades = students[input_user]["Grades"]
        sum_grades = sum(student_grades.values())
        overage_grades = sum_grades/len(student_grades)
        print(f"{input_user} got the follwing grades: ")
        for topic,grade in student_grades.items():
            print(f"{topic}: {grade} ")
        print("_"*60)
        print(f"{input_user} percentage's is {overage_grades:.2f}%")
    else:
        print(f"Sorry we dont have information about {input_user}")






