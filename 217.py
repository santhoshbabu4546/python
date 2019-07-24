#a
eoin,ben=map(int,input().split())
san=input().split()
sai=[]
for o in san:
  if (int(o)%2!=0):
    sai.append(o)
print(sai[ben-1])
