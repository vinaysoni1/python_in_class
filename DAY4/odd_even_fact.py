def even_fact(n):
    ans =1
    for i in range(2, n+1,2):
        ans*=i
        return ans
def odd_fact(n):
    ans =1
    for i in range(2, n+1,2):
        ans*=i
        return ans
    
n=int(input("Enter a number: "))
if n%2==0:
        print(even_fact(n))     
else:
        print(odd_fact(n))  