n=int(input())
a=list(map(int,input().split()))[:n]
c=0
for i in a:
    while(i):
        c+=i%10
        i//=10
print(c)