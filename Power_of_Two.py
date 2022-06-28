a=int(input())
while(a):
    if a%2!=0:
        print(False)
        break
    a=a%2
else:
    print(True)