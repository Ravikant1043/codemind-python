n=int(input())
arr=list(map(int,input().split()))
e=[]
o=[]
for i in range(len(arr)):
    if(arr[i]%2==0):
        e.append(arr[i])
    else:
        o.append(arr[i])
if len(o)>len(e):
    for i in range(len(o)-len(e)):
        e.append(0)
elif len(e)>len(o):
    for i in range(len(e)-len(o)):
        o.append(0)
d=[]
for i in range(len(e)):
    d.append(e[i])
    d.append(o[i])
for i in d:
    if(i==0):
        d.remove(0)
if (len(d)%2==0):
    print(*d)
elif (len(d)%2==1):
    d.append(0)
    print(*d)
    