l=input()
c=0
for i in l:
    if i.isdigit():
        c+=1
print(len(l)-c)