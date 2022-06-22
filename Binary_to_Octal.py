i=int(input())
while(i):
    i-=1
    a=input()
    a='0b'+a
    a=eval(a)
    print(oct(a)[2:])