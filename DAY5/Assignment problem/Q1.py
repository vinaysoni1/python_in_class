# valid email address
email = input("Enter your email address: ")
at_index = email.find("@")
dot_index = email.rfind(".")
if at_index > 0 and dot_index > at_index + 1 and dot_index < len(email) - 1:
    print("Valid email address")
else:
    print("Invalid email address")