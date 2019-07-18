x,y=map(int,input().split())
ab=list(map(int,input().split()[:x]))
if y in ab:
    print('Yes')
else:
    print('No')
