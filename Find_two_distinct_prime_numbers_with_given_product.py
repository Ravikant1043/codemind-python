def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
for i in range(2,n//2+1):
    if n%i==0 and prime(i)==True and prime(n//i)==True:
        print(i,n//i)
        break
else:
    print("-1")