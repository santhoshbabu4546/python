b1,b2=input().split()
b1=int(b1)
b2=int(b2)
l=[]
if(b1>1 and b2>1):
    for k in range (b1,b2+1):
        for t in range (2,k):
            if (k%t==0):
                break
        else:
            l.append(k)
print(len(l))
