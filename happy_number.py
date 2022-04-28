def happy(n):
    if n==1 or n==7:
        print("True")
        return 
    if n==4:
        print("False")
        return 
    n=str(n)
    d=0
    for i in n:
        d+=int(i)**2
    n=int(n)
    happy(d)
    return d
    
n=int(input())
happy(n)