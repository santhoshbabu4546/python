f=[int(j) for j in input().split()]
u=f[0]
p=f[1]
f=[int(j) for j in input().split()]
f.sort()
res=[]
for j in f:
    if(j<p):
        res.append(j)
print(sep=" ",*res)
