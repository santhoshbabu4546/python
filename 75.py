s=int(input())
t=[]
for j in range(s):
  r=input()
  t.append(r)
y=[]
for j in zip(*t):
  if(j.count(j[0])==len(j)):
    y.append(j[0])
  else:
    break
print(''.join(y))
