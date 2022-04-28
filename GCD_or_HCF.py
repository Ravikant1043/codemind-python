import math as m
a,b=map(int,input().split())
g=0
i=1
while(i<=a or i<=b):
    if(a%i==0 and b%i==0):
        g=i
    i+=1
print(g)