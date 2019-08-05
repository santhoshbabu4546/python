#a
x=int(input())
k=[int(j) for j in input().split()]
z=1
m=z
sep=1
for j in range(x-1):
    if(k[j]==k[j+1]):
        z=z+1
        sep=z
    elif(z>m):
        m=z
        sep=z
        z=1
print(sep)
