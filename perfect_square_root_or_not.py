import math as m
def root(n):
    k=m.ceil(m.sqrt(n))
    if(k**2==n):
        return True
    else:
        return False
n=int(input())
if(root(n)==1):
    print("True")
else:
    print("False")