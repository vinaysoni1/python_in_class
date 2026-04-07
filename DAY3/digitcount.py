num = int(input("Enter any number : "))
count = 0
for i in str(num):
    num = num // 10
    count += 1
print(count)

n=str(input("Enter a string:"))
print(len(set(n))) 