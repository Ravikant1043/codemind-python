def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
c=0
for i in range(1,n):
    if n%i==0 and prime(i)==0:
        c+=1
print(c+2)