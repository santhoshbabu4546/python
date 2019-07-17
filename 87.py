from itertools import combinations
s,e=map(int,input().split())
n=len(str(s))
r=list(combinations(str(s),n-e))
r.sort()
print(*r[0],sep='')
