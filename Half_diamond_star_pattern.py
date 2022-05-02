def fo(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
def re(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()
n=int(input())
if n<3:
    print("The pattern is not possible")
else:
    fo(n)
    re(n-1)