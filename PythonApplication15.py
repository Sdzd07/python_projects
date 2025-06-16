#Print the information of the student with the highest total percentage 
students = {
"Mohamed Hassan": {"grades": {
"math": 100,
"english": 90,
"science": 80,
"arabic": 100,
"history": 97},
"school": "Kadri"
},
"Ahmed Kamal": {"grades": {
"math": 100,
"english": 95,
"science": 93,
"arabic": 100,
"history": 94},
"school": "Kadri"
},
"Ali Adel": {"grades": {
"math": 100,
"english": 100,
"science": 100,
"arabic": 100,
"history": 100},
"school": "Kadri"
},
"Hossam Yehia": {"grades": {
"math": 100,
"english": 94,
"science": 98,
"arabic": 100,
"history": 100},
"school": "Kadri"
}
}
hights_percentage = 0
for student in students:
    student_grades = students[student]["grades"]
    average_grades = sum(student_grades.values())/len(student_grades)
    if average_grades>hights_percentage:
       hights_percentage = average_grades          
       student_name = student
print(f"{student_name} has the hights total percentage wish is: {hights_percentage:.2f}")
print("_"*60)
for topic,grade in students[student_name]["grades"].items():
    print(f"{topic.title()}: {grade}")
print("-"*40)
#other solution
students_total_percentage = {}
for student in students:
    grades = students[student]["grades"]
    total_percentage = sum(grades.values())/len(grades)
    students_total_percentage[student] = total_percentage
hight_total_percentage = max(students_total_percentage.values())
for student in students_total_percentage:
    if students_total_percentage[student]== hight_total_percentage:
        print(f"{student} has the hights total percentage wish is: {hight_total_percentage:.2f}")
        print("_"*60)
        student_grades = students[student]["grades"]
        for subject,grade in student_grades.items():
            print(f"{subject.title()}: {grade}")