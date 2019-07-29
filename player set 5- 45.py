#a
w1,r1=map(int,input().split())
x=[(j,u) for j in range(w1) for u in range(w1) if j+u==(w1/2) and j*u==r1]
if len(x)>0:
    print("yes",end='')
else:
    print("no",end='') 
