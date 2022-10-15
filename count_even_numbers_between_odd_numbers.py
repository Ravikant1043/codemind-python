n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if(arr[i-1]%2==1 and arr[i+1]%2==1):
        if(arr[i]%2==0):
            c=c+1
print(c)            
            