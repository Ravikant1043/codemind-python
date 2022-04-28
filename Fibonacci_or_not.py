import math as m
def root(n):
    k=m.ceil(m.sqrt(n))
    if(k**2==n):
        return True
    else:
        return False
n=int(input())
if root(5*n**2 -4)==1 or root(5*n**2 +4)==1:
    print("True")
else:
    print("False")