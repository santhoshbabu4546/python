#a
x=int(input())
h=list(map(int,input().split()))
y=h[0]
for j in h:
  if(h[j]>y):
    y=h[j]
print(y)
