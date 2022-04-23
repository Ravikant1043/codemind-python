import math
n=int(input())
while n:
    a=int(input())
    m=math.ceil(math.sqrt(a))
    if pow(m,2)==a:
        print("True")
    else:
        print("False")
    n-=1