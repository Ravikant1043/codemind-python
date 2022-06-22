i=int(input())
while(i):
    i-=1
    a=(input())
    a='0x'+a
    a=eval(a)
    a=bin(a)[2:]
    if len(a)%4==0:
        print(a)
    elif len(a)%4==1:
        print('000'+a)
    elif len(a)%4==2:
        print('00'+a)
    else:
        print('0'+a)