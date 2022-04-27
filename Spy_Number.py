def add(n):
    d=0
    while(n):
        d+=n%10
        n=n//10
    return d
    
def mul(n):
    d=1
    while(n):
        d=d*n%10
        n=n//10
    return d
n=int(input())
if add(n)==mul(n):
    print("Spy Number")
else:
    print("Not Spy Number")