n=int(input())
t=n-1
for i in range(1,n+1):
    print(" "*t,end="")
    t-=1
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()