def fib(n):
    a=0
    b=1
    i=0
    print(a,b,end=" ")
    while n-2:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        n-=1
    
n=int(input())
fib(n)