a=input()
s=a.split()[::-1]
l=[]
for i in s:
    l.append(i)
print(*l)