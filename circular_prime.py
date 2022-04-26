def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True
n=int(input())
d=0
t=n
while(t):
    i=t%10
    d=d*10+i
    t=t//10
if(prime(n)==1 and prime(d)==1):
    print("circular prime")
elif(prime(n)==1 and prime(d)==0):
    print("prime but not a circular prime")
elif(prime(n)==0):
    print("not prime")