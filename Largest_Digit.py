n=int(input())
k=0
while(n!=0):
    i=n%10
    if(i>k):
        k=i
    n=n//10
print(k)