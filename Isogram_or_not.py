i=input()
i=list(i)
i.sort()
s=set(i)
s=list(s)
s.sort()
if i==s:
    print(True)
else:
    print(False)