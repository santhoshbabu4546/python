def rs(k):
    if(k<=1):
        return (1)
    else:
        return(rs(k-1)+rs(k-2))
k=int(input())
o=[]
for l in range (k):
    o.append(rs(l))
print(*o)
