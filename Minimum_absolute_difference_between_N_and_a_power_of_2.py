n=int(input())
c=0
i=0
while(c<n):
    i+=1
    c=2**i
if(2**(i)==n):
    print("0")
elif abs(2**i-n)>abs(2**(i-1)-n):
    print(abs(2**(i-1)-n))
else:
    print(abs(2**i-n))