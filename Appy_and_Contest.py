t=int(input())
while(t):
    t-=1
    n,a,b,k=map(int,input().split())
    p=n//a
    o=n//b
    c=n//(a*b)
    if p+o-c>=k:
        print("Win")
    else:
        print("Lose")