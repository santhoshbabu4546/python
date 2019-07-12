aa,bb=input().split()
bb=int(bb)
cc=list(map(int,input().split())) 
sum=0
for i in range(0,aa):
  sum+=cc[i]
print(sum)
