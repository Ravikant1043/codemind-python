import math as m
n=int(input())
a=n**2
d=m.ceil(m.log10(n))
a=str(a)
s=len(a)
a=a[d:]
if(int(a)==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")