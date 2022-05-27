n=input()
b='_+-*&^%$#@!={}[]()|:~`?/.<,>'
c=0
for i in n:
    if i in b:
        c+=1
print(c)