a=int(input())
l=list(map(int,input().split()))[:a]
k=int(input())
c=max(l)
for i in l:
    if i+k>=c:
        print(True,end=' ')
    else:
        print(False,end=' ')