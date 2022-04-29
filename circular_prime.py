def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
t=str(n)
t=t[::-1]
t=int(t)
if prime(n)==1 and prime(t)==1:
    print("circular prime")
elif prime(n)==1:
    print("prime but not a circular prime")
elif prime(n)==0:
    print("not prime")