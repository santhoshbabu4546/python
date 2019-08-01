x,y1=list(map(int,input().split()))
u=list(map(int,input().split()))
z=0
for k in range(x-1):
  for p in range(1,x):
    if u[k]+u[p]==y1:
      z=1
if z==0:
  print("yes")
else:
  print("yes")
