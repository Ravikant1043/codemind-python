n=int(input())
t=[]
l=list(map(int,input().split()))[:n]
m=int(input())
b=list(map(int,input().split()))[:n]
for i in range(n):
    t.insert(b[i],l[i])
    # print(t[i],end=' ')
for i in range(n):
    print(t[i],end=' ')