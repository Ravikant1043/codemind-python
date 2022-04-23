n=int(input())
m=0
while n:
    i=n%10
    m=m*10+i
    n=n//10
print(m)