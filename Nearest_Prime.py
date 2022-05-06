def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
while(n):
    n-=1
    a=int(input())
    u=a
    l=a
    if(a>2):
        while(1):
            if prime(u)==True:
                break
            u+=1
        while(1):
            if prime(l)==True:
                break
            l-=1
        if(abs(u-a)==abs(l-a)):
            print(l)
        elif (abs(u-a)>abs(a-l)):
            print(l)
        else:
            print(u)
    else:
        print(2)