a=int(input())
l=list(map(int,input().split()))[:a]
c=l.count(0)
for i in range(c):
    l.remove(0)
    l.append(0)
print(*l)