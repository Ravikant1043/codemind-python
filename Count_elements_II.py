n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
l=0
for i in a:
    if i not in c:
        c.append(i)
for i in b:
    if i not in d:
        d.append(i)
for i in c:
    if i not in d:
        l=l+1
for i in d:
    if i not in c:
        l=l+1
print(l)        