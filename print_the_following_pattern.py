n=int(input())
k=n+64
for i in range(1,n+1):
    for j in range(i,n+1):
        print(chr(k),end=" ")
    k-=1
    print()