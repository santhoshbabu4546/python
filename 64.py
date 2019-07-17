s=int(input())
d=list(map(int,input().split()))
for j in d:
  if d.count(j)==1:
    print(j)
