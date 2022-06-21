n=int(input())
l=list(map(int,input().split()))[:n]
k=1
while True:
    if k in l:
        k+=1
    else:
        break
print(k)