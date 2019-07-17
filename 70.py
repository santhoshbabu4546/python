a,u,o=map(int,input().split())
j=0
sum=0
while j<a:
  sum=sum+u
  u=u+o
  j=j+1
print(sum)
