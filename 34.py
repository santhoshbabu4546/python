def co(k1,k2):
    for k in k1:
        u1=k1.count(k)
    for y in k2:
        u2=k2.count(y)
    if(u1>=u2 or u1<=u2):
        print("yes")
    else:
        print("no")
k1,k2=input().split()
co(k1,k2)
