n=int(input())
s=0
for i in range(1,n+1,1):
    s=s+(1/i)
# print(round(s,2))
print("{:.2f}".format(s))