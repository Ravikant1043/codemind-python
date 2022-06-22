a=int(input())
b=list(map(int,input().split()))[:a]
for i in b:
    if b.count(i)==1:
        print(i)
        break