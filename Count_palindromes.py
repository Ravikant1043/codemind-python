def p(n):
    n=str(n)
    if(n==n[::-1]):
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))[:n]
c=0
for i in a:
    if p(i)==1:
        c+=1
print(c)