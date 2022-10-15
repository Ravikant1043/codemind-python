n=int(input())
arr=list(map(int,input().split()))
b=[]
for i in arr:
    if i not in b:
        b.append(i)
    else:
        continue
c=0    
for i in range(len(b)):
    if(b[i]%2==1):
        c=c+1
print(c)    