def p(n):
    s=0
    p=n
    while p:
       i=p%10
       s=s*10+i
       p=p//10
    if n==s:
        return True
    else:
        return False
    
a=int(input())
b=int (input())
for i in range(a,b+1):
    if p(i):
        print(i,end=" ")