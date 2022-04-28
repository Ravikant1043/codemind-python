n=input()
for i in n:
    d=0
    for j in n:
        if i==j:
            d+=1
    if d==2:
        print("Not Unique Number")
        break
else:
    print("Unique Number")