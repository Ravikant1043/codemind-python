n=int(input())
arr=list(map(int,input().split()))
a,c=map(int,input().split())
b=[]
f=0
for i in range(n):
    if arr[i]<a or arr[i]>c:
        f=1
        b.append(arr[i])
if(f==0):
    print("-1")
else:
    print(min(b))