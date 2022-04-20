import math
p,r,t=map(int,input().split())
c="{:.2f}".format(p*pow(1+r/100,t))
print(c)