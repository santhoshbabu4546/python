x,y,z=map(str,input().split())
z=int(z)
q=len(x)
o=0
for j in range(q):
    if(x[j]!=y[j]):
        o=o+1
if(o==z):
    print("yes")
else:
    print("no")
