a,b=map(int,input().split())
l=list(map(int,input().split()))[:a]
t=list(map(int,input().split()))[:b]
t=list(set(t))
l=list(set(l))
d=0
for i in range(len(t)):
    for j in range(len(l)):
        if l[j]==t[i]:
            # print(l[i])
            d+=1

print(d)