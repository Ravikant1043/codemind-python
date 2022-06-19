n=int(input())
l=list(map(int,input().split()))[:n]
l.sort()
l.reverse()
if n%2==0:
    k=len(l)
else:
    k=len(l)-1
for i in range(0,k-1,2):
    if l[i]>l[i+1]:
        t=l[i]
        l[i]=l[i+1]
        l[i+1]=t
print(*l)