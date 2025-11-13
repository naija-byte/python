'''Binary file member.dat store details of members in a dictionary like
{ memberno : [ name,dept,points] , memberno : [ name,dept,points] }
 memberno     int
name               string
dept                 string
points               float

Define following function below description for student.dat
#) accept () that accept details of N members  and store it in  student.dat .
#)display() that read and display details of members from member.dat , also display no. of members present
  in member.dat
#) add() that accept student details till user choice and add it in student.dat'''

import pickle
def display():
    with open("member.dat","rb") as f:
        a=pickle.load(f)
        print(len(d))
        for i in a:
            print(i,a[i])

def add():
    with open("member.dat","rb") as f:
        a=pickle.load(f)
        while True:
            memberno=
            name=
            dept=
            points=
            a[memberno]=[name,dept,points]
            ch=input("more?")
            if ch==0:
                break
        
    with open("member.dat","wb") as f:
        pickle.dump(a)
'''#) view() that read and display those members whose dept is “cs” and points is more than 80 from member.dat.
#)searchMember(memberno) that read and display member details of members passed as parameter. If not present display error msg.
#)searcName() that accept name from user display its dept & points , if name not present display error msg'''

import pickle
def view():
    with open("member.dat","rb")as f:
        a=pickle.load(f)
        for i in a:
            if a[i][1]=="cs" and a[i][2]>80:
                print(i)
"""#)searcName() that accept name from user display its dept & points , if name not present display error"""


def SeachName():
    
    with open("member.dat","rb")as f:
         a=pickle.load(f)
         name=input()
         for i in a:
             if a[i][0]==name:
                 print(a[i][1],a[i][2])

"""#)Points() that read and display all member name in descending order whose points is 90 to 100 from member.dat
#)search(dept) that taking dept as parameter , display member details of the dept and also display average points of the dept ,
if dept is not present display error msg."""

def Point():
    with open("member.dat","rb")as f:
        a=pickle.load(f)
        l=[]
        for i in a:
            if a[i][2]>90 and a[i][2]<100:load
                l.append(a[i][0])

        l.sort(reverse=True)
        for i in l:
            print(i)
               
def search(dept):
    with open("member.dat","rb")as f:
        a=pickle.load(f)
        d=0
        c=0
        for i in a:
            if a[i][2]==dept:
                print(a[i])
                c+=1
                d+=a[i][1]
        avg=d//c
        print(avg)

'''#)deleteMember() that remove those member details whose member number taken from user as parameter , if not present display Error msg .
also display no of member deleted.'''

def deleteMember():
   
    mem=int(input())
    with open("member.dat","rb")as f:
        a=pickle.load(f)
        if mem in a:
            a.pop(mem)
    with open("member.dat","wb")as f:
        pickle.dump(a)


'''#) remove() that remove the member details of whose points is less than 60 also display no of members deleted from member.dat'''

def remove():
    f=open("member.dat",'rb')
    b={}
    c=0
    a=pickle.load(f)
    for i in a:
        if a[i][2]<60:
            
            c+=1
        else:
            b[i]=a[i]
    print(c)
    f.close()
    f=open("member.dat","wb")
    pickle.dump(b)
    f.close()

"""increasePoints() that increase points of IT Dept of all members by 12 in  member.dat"""

def incpoints():
    f=open("member.dat",'rb')
   
    
    a=pickle.load(f)
    for i in a:
        if a[i][2]=="IT":
            a[i][1]+=12
            
            
            
        
    
    f.close()
    f=open("member.dat","wb")
    pickle.dump(a)
    f.close()


''' read and display member names whose points are more than average points of all members from member.dat'''

def display():
    with open("member.dat","rb")as f:
        a=pickle.load(f)
        c=0
        for i in a:
            c+=a[i][2]
            avg=c//len(a)
        for i in a:
            if a[i][1]>avg:
                print(i,a[i])


        
        

    
                
    
    
        
    
    
                
    


            
            
         
     
