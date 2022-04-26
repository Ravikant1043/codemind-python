a=int(input())
b=int(input())
d=0
c=0
for i in range(1,a):
    if(a%i==0):
        d+=i
for i in range(1,b):
    if(b%i==0):
        c+=i
if(d==b and c==a):
    print("Amicable")
else:
    print("Not Amicable")