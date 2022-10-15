n=int(input())
arr=list(map(int,input().split()))
if(n%2==0):
    for i in range(len(arr)):
        print(arr[i],end=" ")
elif(n%2==1):
        arr.append("0")
        for i in range(len(arr)):
            print(arr[i],end=" ")