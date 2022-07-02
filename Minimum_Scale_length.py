n=int(input())
l=list(map(int,input().split()))[:n]
p=max(l)
for i in range(p,0,-1):
    c=0
    for j in range(n):
        if l[j]%i==0:
            c+=1
    if c==n:
        print(i)
        break