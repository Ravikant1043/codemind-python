def prime(n):
    prime=True
    if(n==1):
        return 0
    if n==2:
        return 1
    else:
        for i in range(2,n):
            if n%i==0:
                prime=False
                break
    if prime:
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
m=max(a)
n=min(a)
i=a.index(m)
j=a.index(n)
c=0
if(i<j):
    i,j=j,i
for k in range(j,i+1):
    if a[k]>=n and a[k]<=m:
        if prime(a[k]):
            c+=1
print(c)