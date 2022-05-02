n=int(input())
j=n-1
for i in range(1,n+1):
    print(" "*j,end="")
    j-=1
    for k in range(i-1,0,-1):
        print(k,end="")
    for p in range(0,i,1):
        print(p,end='')
    print()