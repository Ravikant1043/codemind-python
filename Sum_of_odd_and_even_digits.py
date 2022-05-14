n=int(input())
l=list(map(int,input().split()))[:n]
o=0
e=0
for i in range(n):
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
if o==e:
    print("YES")
else:
    print("NO")