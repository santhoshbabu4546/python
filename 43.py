s1=int(input())
count=0
int=[]
n2=['a','a','b','i','k','l']
for j in range (0,s1):
    int.append(input())
for j in int:
    f=sorted(j)
    if(n2==f):
        count=count+1
print(count)
