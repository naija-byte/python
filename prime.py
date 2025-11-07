n=int(input("Enter a number to check whether it is a prime no. or not: "))
f=0
for i in range(2,n):
    if(n%i==0):
        f+=1
if f>0:
    print("It is not a prime number")
else:
    print("It is a Prime Number")
