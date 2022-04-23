def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

n=int(input())
k=0
while k<n:
    i=int(input())
    print(fac(i))
    k-=1