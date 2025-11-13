s="WATER"
for i in range(0,len(s)):
    print(i*" ",end="")
    print(s[i])


s="WATER"
for i in range(len(s)-1,-1,-1):
    print(i*" ",end="")
    print(s[i])

s="GOGREEN"
space=len(s)-1
for i in range(0,len(s)):
    print(space*" ",end="")
    for j in range(0,i+1):
        print(s[j],end="")
        space-=1
        print()
