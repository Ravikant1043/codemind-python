n=int(input())
p=n
s=0
while p:
    i=p%10
    s=s*10+i
    p=p//10
if s==n:
    print("True")
else:
    print("False")