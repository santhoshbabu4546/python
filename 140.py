x=int(input())
y=list(map(int,input().split()))
b=0
h=len(y)
for i in range(h):
    b+=y[i]
p=b//h
print(p)
