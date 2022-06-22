a,b=map(int,input().split())
l=list(map(int,input().split()))[:a]
c=list(map(int,input().split()))[:b]
for i in c:
    if i not in l:
        print("No")
        break
    else:
        l.remove(i)
else:
    print('Yes')