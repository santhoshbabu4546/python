m3=int(input())
count=0
for j in range(m3):
    m1,m2=map(int,input().split())
    if m1<m2:
        count+=1
print(count,end='') 
