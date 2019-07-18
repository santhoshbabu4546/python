w=input()
u=list(map(int,input().split()))
y=[]
for j in range(len(u)):
  if j % 2 == 0:
    if u[j] % 2 != 0:
      t.append(u[j])
  else:
    if u[j] % 2 == 0:
      y.append(u[j])
for j in y:
  print(j,end=" ")
      
