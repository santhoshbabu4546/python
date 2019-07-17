s,r=list(map(int,input().split()))
t,o=list(map(int,input().split()))
p,q=list(map(int,input().split()))
if s==r or t==o or p==q or s==t==p or r==o==q:
    print('yes')
else:
    print('no')
