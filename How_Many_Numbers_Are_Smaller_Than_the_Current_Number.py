n=int(input())
t=[]
l=list(map(int,input().split()))[:n]
for i in range(n):
    c=0
    for j in range(n):
        if l[i]>l[j] and i!=j :
            c+=1
    t.append(c)
for i in range(n):
    print(t[i],end=' ')