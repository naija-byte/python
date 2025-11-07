n=int(input("Enter a number to check if its an Armstrong no.or not"))
c=n
s=0
count=0
while c>0:
    d=c%10
    count+=1
    c//=10
c=n
while c>0:
    d=c%10
    s+=d**count
    c//=10
if s==n:
    print("Sum :",s)
    print("The no. is an Armstrong no.")
else:
    print("Sum :",s)
    print("The no. is NOT an Armstrong no.")
