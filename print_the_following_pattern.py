n=int(input())
t=n
for i in range(1,n+1):
    for j in range(t-1):
        print(" ",end="")
    t-=1
    for j in range(2*i-1):
        print(i,end="")
    print()
    