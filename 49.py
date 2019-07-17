a=int(input())
b=list(map(int,input().split(None,a)[:a]))
a=[]
for j in range(len(b)):
    if d[j]==j:
        
        a.append(b[j])
if len(a)==0:
    print(-1)
else:
    print(" ".join(map(str,a)))
