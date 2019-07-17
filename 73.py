str = int(input())
ytr = list(map(int,input().split()[:str]))
ray = sorted(ytr)
for j in ray:
    print(j,end=" ")
