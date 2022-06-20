a=int(input())
ct=0
while(a):
    a-=1
    b=int(input())
    l=list(map(int,input().split()))[:b]
    ct=0
    for i in l:
        if i%2!=0:
            ct+=1
    print(ct//2)