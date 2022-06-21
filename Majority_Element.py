n=int(input())
l=list(map(int,input().split()))[:n]
b=[]
for i in l:
    b.append(l.count(i))
k=max(b)
print(l[b.index(k)])