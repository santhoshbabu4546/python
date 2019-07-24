#a
s=input()
y=[]
for j in s:
    if(j.isnumeric()):
        y.append(j)
print(''.join(y))
