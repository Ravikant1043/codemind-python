n=int(input())
s=0
if n>=0:
    while(n):
        d=n%10
        s=s*10+d
        n=n//10
    print(s)
else:
    n=(-n)
    while(n):
        d=n%10
        s=s*10+d
        n=n//10
    print(-s)