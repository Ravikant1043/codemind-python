n=input()
o=0
e=0
for i in n:
    if (int(i)%2)==0:
        e=1
    else:
        o=1
if e==1 and o==1:
    print("Mixed")
elif e==1 and o==0:
    print("Even")
elif e==0 and o==1:
    print("Odd")