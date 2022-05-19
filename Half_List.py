n=int(input())
l=list(map(int,input().split()))[:n]
t=n//2
k=[]
for i in range(t):
    k.append(l[n-1-i])
for i in range(t):
    l[t+i]=l[i]
    l[i]=k[i]
for i in range(n):
    print(l[i],end=' ')