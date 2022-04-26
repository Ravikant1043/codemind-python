n=int(input())
t=n
d=0
while(t):
    i=t%10
    d+=i
    t=t//10
    
if(n%d==0):
    print("True")
else:
    print("False")