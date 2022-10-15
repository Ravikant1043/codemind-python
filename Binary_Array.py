n=int(input())
arr=list(map(int,input().split()))
f=0
for i in range(len(arr)):
    if(arr[i]==0 or arr[i]==1):
        f=f+1
if(f==n):
    print("True")
else:
    print("False")