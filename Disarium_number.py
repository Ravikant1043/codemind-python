import math as m
n=int(input())
t=n
d=0
k=m.ceil(m.log10(n))
while(t):
    i=t%10
    d+=i**k
    t=t//10
    k-=1
if d==n:
    print("True")
else:
    print("False")