import math as m
def square(n):
    k=m.ceil(m.sqrt(n))
    if m.pow(k,2)==n:
        return True
    else:
        return False

n=int(input())
if(square(5*n**2 +4)==1 or square(5*n**2 -4)==1):
    print("True")
else:
    print("False")