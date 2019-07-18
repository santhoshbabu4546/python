dc=list(map(int,input().split()))
r=-10
for j in range (10):
    if(dc[j]>r):
        r=dc[j]
print(r)
