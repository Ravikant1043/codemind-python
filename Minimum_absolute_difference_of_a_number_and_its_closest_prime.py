def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True

n=int(input())
i=n
while(1):
    if prime(i)==1:
        break
    i+=1
t=n-1
while(1):
    if prime(t)==1:
        break
    t-=1
if(abs(n-i)>abs(t-n)):
    print(abs(t-n))
else:
    print(abs(n-i))