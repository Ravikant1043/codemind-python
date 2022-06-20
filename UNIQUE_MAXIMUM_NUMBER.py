a=int(input())
k=0
b=[0]
l=list(map(int,input().split()))[:a]
for i in range(len(l)):
    if l.count(l[i])==1:
        b.append(l[i])
        k=1
b.sort()
if k==0:
    print(-1)
else:
    print(b[-1])