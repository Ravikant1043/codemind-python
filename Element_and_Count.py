n=int(input())
arr=list(map(int,input().split()))
b=[]
for i in arr:
    if i not in b:
        b.append(i)
    else:
        continue
c=[]
for i in range(len(b)):
    c.append(b[i])
    d=arr.count(b[i])
    c.append(d) 
print(*c)      
    