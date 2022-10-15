n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(len(arr)):
    arr.append(arr[0])
    break
for i in range(len(arr)):
    arr=arr[::-1]
    arr.append(arr[n-1])
    break
for i in range(0,n+1):
    if(arr[i-1]%2==0 and arr[i+1]%2==1)or(arr[i-1]%2==1 and arr[i+1]%2==0):
            c=c+1
print(c)            