a=int(input())
while(a):
    a-=1
    b=int(input())
    b=bin(b)[2:]
    print(b.count('1'))