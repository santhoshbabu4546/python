#a
r1=int(input())
r2=[]
for v in range(0,r1):
    r2.append(list(map(int,input().split())))
z=0
k=0
for v in range(0,r1):
    for j in range(0,r1):
        if r2[v][j]==1:
            if v!=r1-1 and r2[v+1][j]==0:
                z=z+1
            if j!=r1-1 and r2[v][j+1]==0:
                z=z+1
            if v!=0 and r2[v-1][j]==0:
                z=z+1
            if j!=0 and r2[v][j-1]==0:
                z=z+1
            if v==0 and j==0 or v==r1-1 and j==r1-1  or v==0 and j==r1-1 or v==r1-1 and j==0 and z==2:
                k=k+1
            elif v==1 and j>0 and j<d-1 and z==3:
                k=k+1
            elif z==4:
                k=k+1
        z=0
                
print(k)
