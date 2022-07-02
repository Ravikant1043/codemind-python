a=input()
k=0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[i]==a[j] and i!=j:
            c=1
            break
    if c==0:
        print(i)
        k=1
        break
if k==0:
    print(-1)