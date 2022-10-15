n=int(input())
arr=list(map(int,input().split()))
a=[]
b=[]
for i in range(len(arr)):
    if(arr[i]%2==1):
        a.append(arr[i])
    elif(arr[i]%2==0):
        b.append(arr[i])
for i in range(len(a)):
    print(a[i],end=" ")
for i in range(len(b)):
    print(b[i],end=" ")