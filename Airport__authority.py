n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
t=int(input())
d=0
for i in range(n):
    if(l[i]>t):
        d=d+2
    else:
        d+=1
print(d)