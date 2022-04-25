n=int(input())
k=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j or i+j==n+1):
            print(k ,end=" ")
        else:
            print(" ",end="")
    print()
    k=k-1