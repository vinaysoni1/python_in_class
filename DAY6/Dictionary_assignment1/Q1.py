# Q.1 wap to crete dictionary named student_grades with 5 students and their grades. Then print the name of students whose grade is greater than 80.
student_grades = {
    "Alice": 85,
    "Bob": 78,  
    "Charlie": 92,
    "David": 88,
    "Eve": 79
}
print("Students with grades greater than 80:")
for student, grade in student_grades.items():
    if grade > 80:
        print(student)  

print(student_grades)        