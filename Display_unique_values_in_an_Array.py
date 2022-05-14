n=int(input())
l=list(map(int,input().split()))[:n]
t=5
for i in range(n):
    c=0
    for j in range(n):
        if l[i]==l[j] and i!=j:
            c+=1
            break
    if c==0:
        print(l[i],end=' ')
        t=4
if t==5:
    print("-1")