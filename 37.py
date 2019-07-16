a1,b2=map(int,input().split())
d3=list(map(int,input().split()))
for i in range (0,b2):
    d3=[d3[-1]]+d3[:-1]
print(*d3,end='')
