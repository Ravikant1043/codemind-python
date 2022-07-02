s=input().split()
for i in s:
    if(s.index(i)%2==0):
        print(i[::-1],end=" ")
    else:
        print(i,end=" ")