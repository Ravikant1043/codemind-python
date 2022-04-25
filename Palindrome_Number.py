n=int(input())
while n:
    d=0
    n=n-1
    i=int(input())
    p=i
    while(i):
        k=i%10
        d=d*10+k
        i=i//10
    if(d==p):
        print("True")
    else:
        print("False")