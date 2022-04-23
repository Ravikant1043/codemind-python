n=int(input())
m=0
while n:
    i=n%10
    if m<i:
        m=i
    n=n//10
print(m)