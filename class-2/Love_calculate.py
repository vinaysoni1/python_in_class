print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Combine names and convert to lowercase for consistency
combined_names = (name1 + name2).lower()

# Count occurrences of letters in 'TRUE'
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
first_digit = t + r + u + e

# Count occurrences of letters in 'LOVE'
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
second_digit = l + o + v + e

# Combine the two counts into a single score
score = int(str(first_digit) + str(second_digit))

# Output results with a fun message
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
