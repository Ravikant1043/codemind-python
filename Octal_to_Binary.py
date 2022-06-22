i=int(input())
while(i):
    i-=1
    a=input()
    a='0o'+a
    a=eval(a)
    print(bin(a)[2:])