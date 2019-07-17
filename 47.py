n1=int(input())
a=list(map(int,input().split()))
ln=[]
for j in a:
    if a.count(j)>1:
        if str(j) not in ln:
            ln.append(str(j))
if len(ln)==0:
    print("unique")
else:
    print(" ".join(ln))
