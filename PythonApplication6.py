#print student's info in the folwing in format
#Student name: Ahmed Hassen 
#School: Rahimi 
#Grades: 
#Math : 100
#Arabic: 100
#History: 90 
students = {
    "Ahmed Hassen": {"Grades": {
        "Math": 100, 
        "Arabi": 100, 
        "History": 90, 
        "English": 95,
        "Sience": 90
        },
        "School":"Rahimi" 
    },
    "Ahmed kamel": { "Grades":{
        "Math": 90,
        "Arabic": 100,
        "History": 85,
        "English": 100,
        "Sience": 97
        },
        "School": "kadri"
    }
}
for student in students:
    print(f"Student name: {student} ")
    print(f'School: {students[student]["School"]}')
    print("Grades: ")
    for grade in students[student]["Grades"]:
            print(f'{grade}: {students[student]["Grades"][grade]}')
    print("_"*40)
        



