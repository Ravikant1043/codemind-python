n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(len(arr)):
    s=sum(arr)
avg=s//n
c=0
for i in range(len(arr)):
    if(arr[i]<=int(avg)):
         c=c+1
print(c)    