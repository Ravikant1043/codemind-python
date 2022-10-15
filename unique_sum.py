n=int(input())
arr=list(map(int,input().split()))
b=[]
for i in arr:
    if i not in b:
        b.append(i)
    else:
        continue
s=0    
for i in range(len(b)):
    s=s+b[i]
print(s)    
    