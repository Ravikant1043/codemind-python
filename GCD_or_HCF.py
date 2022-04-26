a,b=map(int,input().split())
if a>b:
    k=a
else:
    k=b
for i in range(1,k+1):
    if(a%i==0) and b%i==0:
        g=i
print(g)