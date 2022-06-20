a=int(input())
l=list(map(int,input().split()))[:a]
b=[]
for i in range(0,len(l),2):
    for j in range(l[i]):
        b.append(l[i+1])
print(*b)