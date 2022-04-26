a=int(input())
b=int(input())
for i in range(a,b+1):
    n=i
    k=0
    while(n):
        d=n%10
        if(d==0):
            k=0
            break
        if(i%d)==0:
            k=1
        else:
            k=0
            break
        n=n//10
    if k==1:
        print(i,end=" ")