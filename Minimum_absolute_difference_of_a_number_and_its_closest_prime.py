def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
if n==2 or prime(n)==1:
    print("0")
else:
    i=n+1
    while(1):
        if prime(i)==1:
            break
        i+=1
    t=n-1
    while(1):
        if prime(t)==1:
            break
        t-=1
    if abs(i-n)>abs (n-t):
        print(abs(n-t))
    else:
        print(abs(i-n))