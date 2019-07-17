r,t=map(int,input().split())
for j in range(r+1,t):
  sum=0
  h=j
  while h>0:
    s=h%10
    sum=sum+s**3
    h=h//10
    if (sum==j):
      print(j,end=" ")
