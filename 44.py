rs1=int(input())
l2=[]
for j in range (2,rs1+1):
    if(rs1%j)==0:
        l2.append(j)
        rs1=rs1//j
o=sorted(l2)
print(*o)
