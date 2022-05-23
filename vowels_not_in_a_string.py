n=input()
a='aeiou'
b=[]
k=0
for i in n:
    if i in a and i not in b:
        b.append(i)
for i in a:
    if i not in b:
        print(i,end=' ')
        k=1
if k!=1:
    print(0)