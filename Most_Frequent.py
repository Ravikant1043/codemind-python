n=int(input())
l=list(map(int,input().split()))[:n]
k=set(l)
b=[]
for i in k:
    b.append(l.count(i))
k=list(k)
n=b.index(max(b))
print(k[n])