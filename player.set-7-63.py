d=int(input())
s=list(map(int,input().split()))
r=list(map(int,input().split()))
s=set(s)
r=set(r)
if(s & r):
  u=sorted(s&r)
  print(*u,abc=' ')
