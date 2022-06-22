a=int(input())
a=bin(a)[2:]
a=list(a)
d={'1':'0','0':'1'}
b=''
for i in a:
   b=b+d[i]
print(eval('0b'+b))