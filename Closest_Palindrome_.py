def ty(n):
    t=n
    d=0
    while(t):
        i=t%10
        d=d*10+i
        t=t//10
    if(d==n):
        return True
    else:
        return False
n=int(input())
i=n-1
while(1):
    if(ty(i)==1):
        break
    i-=1
t=n+1
while(1):
    if(ty(t)==1):
        break
    t+=1
if(abs(t-n)>abs(i-n)):
    print(i)
elif(abs(t-n)==abs(i-n)):
    if(n>t):
        print(t,end=" ")
        print(i,end=" ")
    else:
        print(i,end=" ")
        print(t,end=" ")
else:
    print(t)