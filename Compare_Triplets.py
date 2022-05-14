l=list(map(int,input().split()))[:3]
k=list(map(int,input().split()))[:3]
a=0
b=0
for i in range(3):
    if l[i]>k[i]:
        a+=1
    elif l[i]<k[i]:
        b+=1
print(a,b)