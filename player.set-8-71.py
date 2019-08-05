#a
x=int(input())
z=list(map(int,input().split()))
z.append(-1)
li=[]
for j in range(x-1):
    li.append(max(z[j],z[j+1]))
if(x==1):
    print(z[0])
else:
    for j in range(len(li)-1):
        print(li[j],end=' ')
    print(li[len(li)-1])
