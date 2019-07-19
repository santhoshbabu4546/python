y=int(input())
u=[]
for j in range(1,y+1):
    if(j%2==0):
      if(y%j==0):
         u.append(j)
print(*u,end="")
