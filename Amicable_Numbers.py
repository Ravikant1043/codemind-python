def facsum(n):
    k=0
    for i in range(1,n):
        if n%i==0:
            k+=i
    return k
a=int(input())
b=int(input())
if(b==facsum(a) and a==facsum(b)):
    print("Amicable")
else:
    print("Not Amicable")