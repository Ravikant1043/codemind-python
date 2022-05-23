v='AEIOUaeiou'
n=input().split()
c=0
b=[]
for i in n:
    c=0
    for j in i:
        if j in v:
            c+=1
    b.append(c)
print(max(b))