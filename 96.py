a,b=input().split()
o=abs(len(b)-len(a))
for j in range(len(a)):
    if(len(b)==1 and b[j] in a):
        break
    if(a[j]!=b[j]):
        h=h+1
print(h)
