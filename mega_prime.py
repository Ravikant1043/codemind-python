def prime(n):
    if(n==1):
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
k=0
if(prime(n)==True):
    while(n):
        i=n%10
        if(prime(i)==0):
            k=1
            break
        n=n//10
else:
    k=1
if(k==1):
    print("Not Mega Prime")
else:
    print("Mega Prime")
        