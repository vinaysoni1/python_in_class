# wap to check if key is present in the dictionary or not and print the appropriate message.
student_grades = {
    "Alice": 85,
    "Bob": 78,  
    "Charlie": 92,  
    "David": 88,
    "Eve": 79
}
key_to_check = "Bob"
if key_to_check in student_grades:
    print(f"{key_to_check} is present in the dictionary.")
else:
    print(f"{key_to_check} is not present in the dictionary.")