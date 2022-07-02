def ug(n):
    while(n%2==0):
        n//=2
    if n==1:
        return 1
    while n%3==0:
        n//=3
    if n==1:
        return 1
    while n%5==0:
        n//=5
    if n==1:
        return 1
    return 0
n=int(input())
if ug(n)==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")