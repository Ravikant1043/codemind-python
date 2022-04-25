n=int(input())
while(n):
    n=n-1
    j=0
    a,b=map(int,input().split())
    for i in range(a,b+1):
        if(i%10==3 or i%10==2 or i%10==9):
            j+=1
    print(j)