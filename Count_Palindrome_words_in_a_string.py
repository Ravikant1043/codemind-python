i=input().lower()
i=list(i.split(' '))
c=0
for j in i:
    if j == j[::-1]:
        c+=1
print(c)