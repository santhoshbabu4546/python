#a
x,h=map(int,input().split())
u=[int(j) for j in input().split()]
for j in range(h):
    u.pop()
print(sep=" ",*u)
