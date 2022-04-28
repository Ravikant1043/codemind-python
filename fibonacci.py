n=int(input())
print("0 1 ",end="")
a=0
b=1
c=0
i=0
while(i<n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    i+=1