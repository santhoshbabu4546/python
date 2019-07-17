s,t=map(int,input().split())
for j in range(1,min(s,t)+1):
    if((s%j==0) and (t%j==0)):
        y=j
print(y)
