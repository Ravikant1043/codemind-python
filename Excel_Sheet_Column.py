n=int(input())
o=''
while(n):
    i=(n-1)%26
    o+=chr(i+ord('A'))
    n=(n-1)//26
print(o[::-1])