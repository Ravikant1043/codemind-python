a=input()
c=[]
for i in a:
    c.append(a.count(i))
p=max(set(c))
c=set(c)
c.remove(p)
d=[]
for i in a:
    if a.count(i) in c:
        print(i)
        break
if len(c)==0:
    print(-1)