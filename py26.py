#Print the students’ names and grades in the following form.
#Student: Mohamed 
# Grades: 96, 78, 82, 80
#  -------------------- 
# Mohamed has an average grade of 84.00
student_names = ["Mohamed", "Ahmed", "Ali", "Sara"] 
student_grades = [[96, 78, 82, 80], [86, 92, 98, 90], [76, 88, 90, 72], [78, 86, 98, 88]]
[76, 88, 90, 72], [78, 86, 98, 88]
#Student: Mohamed 
# Grades: 96, 78, 82, 80
#  -------------------- 
# Mohamed has an average grade of 84.00
for i in range(len(student_names)):
    average= sum(student_grades[i])/len(student_grades[i])
    print(f"Student name: {student_names[i]}")
    print("Grades:"), 
    print(*student_grades[i], sep=",")
    print(f"{student_names[i]} has an average grade of {average:.2f}\n-----------------------------------------")  
#second way 
for student, grade in zip(student_names,student_grades):
    average = sum(grade)/len(grade)
    print("Student name:", student)
    print("Grades:")
    print(*grade, sep=",")
    print(f"{student} has an average grade of {average:.2f}\n--------------------------------------")