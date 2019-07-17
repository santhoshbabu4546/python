x,y=map(str,input().split())
z=abs(len(x)-len(y))
for j in range(len(x)):
    if(len(y)==1 and y[j] in x):
        break
    if(x[j]!=y[j]):
        z=z+1
print(z)
