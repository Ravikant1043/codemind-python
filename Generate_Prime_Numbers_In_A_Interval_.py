def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
b=int(input())
if a==1:
    a+=1
for i in range(a,b):
    if prime(i)==1:
        print(i)