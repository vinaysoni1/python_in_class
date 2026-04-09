def fact(n):
    ans =1
    for i in range(1, n+1):
        ans*=i
        return ans
    
n=int(input("Enter a number: "))
r=int(input("Enter a number: "))
if r>n:
    print("Invalid")
else:
    nPr=fact(n)//fact(n-r)
    print(nPr)    