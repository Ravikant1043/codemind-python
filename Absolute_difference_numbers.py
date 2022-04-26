a,b=input().split()
b=int(b)
x=a[:b]
x=int(x)
t=len(a)
y=a[t-b:]
y=int(y)
print(abs(x-y))