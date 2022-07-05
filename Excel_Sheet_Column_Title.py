n=int(input())
t='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'
while(n):
    i=n%26
    if i==0:
        t+='Z'
    else:
        t+=chr(64+i)
    n/=26
    n=int(n)
print(t[::-1])