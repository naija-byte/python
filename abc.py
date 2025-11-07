
"""waf createfile() that accept n as argument and store n lines in mytext.txt
waf display() that read and display no of alphabet,digit,uppercase,lowercase char present in mytext.txt.
waf words() that read and display words having length more than 3 chars and ends with '.' from mytext.txt.
waf lines() that read and display those lines start with  vowels from mytext.txt .

using menu driven program call the above functions."""

def createfile(n):
    with open ("mytext.txt","w") as f:
          for i in range(n):
              s=input("enter line")
              f.write(s+"\n")


def display():
     with open ("mytext.txt","r") as f:
         a=f.read()
         x,b,c,d=0,0,0,0
         for i in a:
             if i.isalpha():
                 x+=1
             if i.isdigit():
                 b+=1
             if i.isupper():
                 c+=1
             if i.islower():
                 d+=1
         print(x,b,c,d)


def words():
   with open ("mytext.txt","r") as f:
       a=f.read()
       b=a.split()
       for i in b:
           if len(i)>3 and i[-1]==".":
               print(i)
def odd():
   with open ("mytext.txt","r") as f:
       a=f.readlines()
       
       for i in a:
           if i[0] in "aeiouAEIOU":
               print(i)

while True:
    print("c:create d:display w:words o:odd e:exit")
    x=input("enter")
    if x=="c":
        n=int(input("enter"))
        createfile(n)
    elif x=="d":
         display()
    elif x=="w":
        words()
    elif x=="o":
        odd()
    elif x== "e":
        break
    
    
            
       
            
                 


            
       
            
                 
