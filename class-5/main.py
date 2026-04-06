 # Comments, Escape Sequences & Print Statement 
# This is a comment, it is ignored by the interpreter
# Comments are used to explain code and make it more readable

#multiple line comment 

'''my name is vinay soni
i am a python developer
i love coding'''


#Escape Sequences
# \n - New Line
#example
print("NAME: Vinay Soni\nAGE: 19\nCITY: Jabalpur")
# \'
print("i am a \"good\" boy")
print("i am a \'good\' boy")

#other parameter in print statement

#end parameter
print("Hello", end=" world !! \n")

#sep parameter
print("Python", "is", "awesome", sep="-")
print("dd", "mm", "yyyy", sep="/")
print("apple", "banana", "cherry", sep=", ")

p=5
if(p>0):
    print("\"p is positive\"")
else:
       print(" \"p is negative\"")
 

x = 5
y = 10

# Swap in one line
x, y = y, x

print(f"x: {x}, y: {y}")  # Output: x: 10, y: 5
    
