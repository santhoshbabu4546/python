x=input()
y=x.strip()
z=1
for j in range (len(y)):
    if(y[j]==' ' and (y[j]!=y[j+1])):
        z=z+1
if(z>1):
    print(z)
