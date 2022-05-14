n=int(input())
c=0
a=list(map(int,input().split()))[:n]
for i in a:
    if len(str(i))%2==0:
        c+=1
print(c)