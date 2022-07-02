def r(n):
    a=0
    while(n):
        i=n%10
        a=a*10+i
        n//=10
    return a
def p(n):
    if str(n)[::-1]==str(n):
        return 1
    return 0

a=int(input())
b=r(a)
a+=b
if p(a):
    print(a)
else:
    b=r(a)
    a+=b
    if p(a):
        print(a)
    else:
        b=r(a)
        a+=b
        print(a)