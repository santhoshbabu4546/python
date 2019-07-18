sb=int(input())
r=input("")
r=list(r.split(" "))
y=[]
for j in range(0,len(r)):
  for d in range(j+1,len(r)):
    if r[j]==r[d]:
      y.append(r[j])
if(len(y)==0):
  print("unique")
else:
  print(y[0])
