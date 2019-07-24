sams,god=map(int,input().split())
son=list(map(int,input().split()[:god]))
zag=[]
for j in son:
   if(j<=j+1):
     zag.append(j)
print(zag[god-1])  
