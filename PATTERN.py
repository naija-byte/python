

"""1"""
x=int(input("Enter a value for the sequence: "))
n=int(input("Enter number of terms: "))
d=1
i=1
s=0
for j in range (1, n+1):
    f=1
    for c in range(1,d+1):
        f*=c
p=(x**i)/f
print(p,end="+")
s+=p
d+=1
i+=1
print("=",s)


"""2"""

x=int(input("Enter a value for the sequence: "))
n=int(input("Enter number of terms: "))
d=1
i=1
s=0
for j in range (1, n+1):
    f=1
    for c in range(1,d+1):
        f*=c
    p=(x**i)/f
    if(j%2==0):
        print(p,end="+")
        s-=p
    else:
        print(p,end="-")
    s+=p
    d+=1
    i+=1
print("=",s)




