n=input()
v='AEIOUaeiou'
b=[]
for i in n:
    if i in v and i not in b:
        b.append(i)
print(*b)