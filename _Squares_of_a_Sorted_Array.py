n=int(input())
t=[]
l=list(map(int,input().split()))[:n]
for i in range(n):
    t.append(l[i]**2)
(t.sort())
for i in range(n):
    print(t[i],end=" ")