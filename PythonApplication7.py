#make program print the studet's inforamtion in this format :
#Ahmed Hassen total percentage :
#-------------------------------
# Mohamed kamel total percentage :
#-------------------------------
#Ali Ahmed total persentage : 
students = { 
    "Ahmed Hassen": {
        "Grades":{
            "Math": 100, 
            "Arabic": 100, 
            "Sience": 90, 
            "History": 97
            },
        "School": "Kadri",
     },
        "Mohamed Kamel":{
        "Grades": {
            "Math": 99, 
            "Arabic": 100, 
            "Sience": 90, 
            "History": 80
            },
        "School": "Rahimi"
     },
     "Ali Ahmed":{
         "Grades":{
             "Math": 90,
             "Arabic": 100, 
             "Sinece": 80, 
             "History": 89
             },
        "School": "kadri"
        }                             
}
#initiliaze for loop to for calculate average students grades 
for student in students:  
    grades = students[student]["Grades"]
#make variable for know the lenght of grades and variable for sum the total grades  
    total_grades = 0    
    lenght_grades = 0
#initialize for loop for over grades     
    for grade in grades:
#increment by lenght by one, and total_grades by each grade          
        total_grades+= grades[grade]
        lenght_grades+=1
#calculate average grades    
        average_grades = total_grades/lenght_grades
    print(f"{student} student's persentage' grades is {average_grades}%")
    print("_"*60)
##################################################################################
#other solution 
#initiliaze for loop to for calculate average students grades 
for student in students:  
    student_grades = (students[student]["Grades"].values())
    sum_grades = sum(student_grades)
#calculate the average grades    
    average_grades = sum_grades/len(student_grades)
    print(f"{student} student's persentage' grades is {average_grades}%")
    print("_"*60)




