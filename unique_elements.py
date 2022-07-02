def printDistinct(arr, n):
    for i in range(0, n):
        d = 0
        for j in range(0, i):
            if (arr[i] == arr[j]):
                d = 1
                break
        if (d == 0):
            print(arr[i],end=" ")
     
n=int(input())
arr=list(map(int,input().split()))[:n]
l=len(arr)
printDistinct(arr, l)