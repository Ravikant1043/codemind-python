s=input()
l=input()
c=0
a=[]
b=[]
for i in s.split():
    if s.count(i)==1:
        a.append(i)
for j in l.split():
    if l.count(j)==1:
        b.append(j)
for i in a:
    for j in b:
        if(i.lower()==j.lower()):
            c=c+1
print(c)            
            