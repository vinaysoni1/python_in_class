# While condition example1
n=int(input("\nEnter a number:"))
for i in range(2, n//2):
    if n%i==0:
        print("not prime")
else:
    print("prime")  


