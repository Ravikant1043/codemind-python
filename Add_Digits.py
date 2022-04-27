import math as m
def add(n):
    d=0
    while(n!=0):
        d=d+n%10
        n=n//10
    return d
n=int(input())
t=m.ceil(m.log10(n))
while(t!=1):
    n=add(n)
    t=m.ceil(m.log10(n))
print(n)