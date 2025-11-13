s=input("Enter a sentence:")
v=0
c=0
d=0
for i in s:
    if i.isalpha():
        if i in "aeiouAEIOU":
            v+=1
            else:
                c+=1
    elif i.isdigit():
        d+=1
print("VOWELS=",v)
print("CONSONANTS=",c)
print("DIGITS=",d)
