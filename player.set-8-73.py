#a
x,y=map(int,input().split())
h=list(map(int,input().split()))
g=x-1
for j in h:
  if(h[j]==y):
    g=j
print(g+1)
