g,f,d=input().split()
g=int(g)
f=int(f)
o=int(o)
sum=0
j=0
while j<g:
	sum=sum+f
	f=f+o
	j=j+1
print(sum)
