# wap will be take list of integer input from user and increse all even number by 5 and decrease all odd number by 5
list = eval(input("Enter a list: "))
newlist=[]
for num in list:
    if num%2!=0:
        newlist.append(num+5)
    else:
        newlist.append(num-5)   
print(newlist)        