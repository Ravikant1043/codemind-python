n=int(input())
t=n**2
t=str(t)
v=len(str(n))
v=len(t)-v
t=t[v:]
t=int(t)
if(t==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")