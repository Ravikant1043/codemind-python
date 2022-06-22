a=int(input())
l=list(map(int,input().split()))[:a]
k=int(input())
p=len(l)-1
try:
    print(l.index(k),end=' ')
    print(p-l[::-1].index(k))
except:
    print(-1,-1)