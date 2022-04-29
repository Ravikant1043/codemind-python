n=int(input())
a=n
d=0
while(n):
    d+=n%10
    n=n//10
if a%d==0:
    print("True")
else:
    print("False")