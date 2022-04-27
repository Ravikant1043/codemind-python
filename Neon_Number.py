def add(n):
    d=0
    while(n):
        d+=n%10
        n=n//10
    return d
n=int(input())
t=n**2
if(add(t)==n):
    print("Neon Number")
else:
    print("Not Neon Number")