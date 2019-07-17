sb=list(map(str,input()))
e=t=0
for k in range(0,len(sb)-1):
  r=sb[k]
  if int(r)!=0:
   for l in range(k+1,k+2):
    r=r+sb[l]
    if int(r)<27 and int(r)>0: e=e+1
    elif int(r)==0: e=e-1
    else: break
if e!=1: t=e%2
print(e+t+1)
