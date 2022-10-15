n=int(input())
arr=list(map(int,input().strip().split()))
s1=0
s2=0
for i in range(0,len(arr)//2):
    s1=s1+arr[i]
for i in range(len(arr)//2,len(arr)):
    s2=s2+arr[i]
print(s1)
print(s2)