x=input()
x.split()
x=x.replace(" ","")
y=[j for j in x if x.count(j)==1]
z=' '.join(y)
print(z.lower())
