n=int(input())
l=list(map(int,input().split()))[:n]
c=0
for i in l:
    if i%2==1:
        c+=1
if c<=2:
    print("YES")
else:
    print("NO")