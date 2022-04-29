n=int(input())
d=0
a=n
for i in range(len(str(n)),0,-1):
    d+=(n%10)**i
    n=n//10
if d==a:
    print("True")
else:
    print("False")