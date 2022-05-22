def p(n):
    n=str(n)
    return int(n[::-1])
n=int(input())
a=list(map(int,input().split()))[:n]
for i in a:
    print(p(i),end=' ')