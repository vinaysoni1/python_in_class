#wapa to delete a key named "Bob" from the existing dictionary named student_grades and then print the updated dictionary.
student_grades = {
    "Alice": 85,
    "Bob": 78,  
    "Charlie": 92,  
    "David": 88,
    "Eve": 79
}
del student_grades["Bob"]
print("Updated student grades:", student_grades)