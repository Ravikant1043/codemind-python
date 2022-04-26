n=int(input())
d=0
for i in range(1,n):
    if(n%i==0):
        d+=i
if d>n:
    print("True")
else:
    print("False")