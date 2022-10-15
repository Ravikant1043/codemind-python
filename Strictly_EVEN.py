n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if(arr[i]%2==0):
        if i%2==1:
            print("False")
            quit()
print("True")            