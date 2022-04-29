def happy(n):
    if (n==1 or n==7):
        print("True")
        return 
    elif n==4:
        print("False")
        return 
    d=0
    while(n):
        d+=(n%10)**2
        n=n//10
    n=d
    happy(n)
n=int(input())
happy(n)