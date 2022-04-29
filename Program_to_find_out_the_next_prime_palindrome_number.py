def p(n):
    t=str(n)
    t=t[::-1]
    if int(t)==n:
        return True
    else:
        return False
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
n+=1
while(1):
    if p(n)==1 and prime(n)==1:
        break
    n+=1
print(n)