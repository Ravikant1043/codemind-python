a=input().lower()
b=input().lower()
a=a.replace(' ','')
b=b.replace(' ','')
l=[]
for i in a:
    if i in b:
        l.append(i)
for i in b:
    if i in a:
        l.append(i)
print(len(set(l)))