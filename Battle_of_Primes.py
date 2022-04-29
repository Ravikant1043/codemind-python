def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
b=int(input())
c=a+b
c+=1
while(1):
    if prime(c)==1:
        break
    c+=1
print(c-a-b)