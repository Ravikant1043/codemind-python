n=int(input())
while(n):
    n-=1
    a=input()
    for i in a:
        if i.isdigit():
            print("Yes")
            break
    else:
        print("No")