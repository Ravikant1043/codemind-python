def adam(n):
    t=n**2
    m=str(n)[::-1]
    p=int(m)**2
    if(str(t)[::-1]==str(p)):
        print("True")
    else:
        print("False")
n=int(input())
adam(n)