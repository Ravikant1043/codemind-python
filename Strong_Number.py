def fac(n):
    d=1
    for i in range(1,n+1):
        d=d*i
    return d
    
a=int(input())
t=a
p=0
while(t):
    # i=t%10
    p+=fac(t%10)
    t=t//10
if p==a:
    print("The number",a,"is a strong number")
else:
    print("The number",a,"is not a strong number")