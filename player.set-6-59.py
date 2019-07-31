k1=int(input())
p=str(input())
t=""
u=""
for j in range(len(p)):
    if p[j]=='1':
        t=t+p[j]+" "
    elif p[j]=='0':
        u=u+t
        t=""
print(u.strip())
